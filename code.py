import streamlit as st
import cv2
import numpy as np
import matplotlib.pyplot as plt
from skimage.metrics import structural_similarity as ssim
import math

# 1. Calcul des métriques avec correction du nom de variable
def calculate_metrics(img1, img2):
    mse = np.mean((img1 - img2) ** 2)
    psnr = 100 if mse == 0 else 20 * math.log10(255.0 / math.sqrt(mse))
    # حساب SSIM
    score, _ = ssim(img1, img2, full=True)
    return mse, psnr, score # نرجِع القيم الثلاث

# 2. Smart CLAHE (AI Suggestion)
def get_auto_params(img):
    std_dev = np.std(img)
    if std_dev < 30: return 4.0, 12
    elif std_dev < 50: return 2.0, 8
    else: return 1.2, 4

# 3. Histogramme avec remplissage bleu (Area plot)
def plot_styled_histogram(img, title):
    hist, _ = np.histogram(img.flatten(), 256, [0, 256])
    cdf = hist.cumsum()
    cdf_normalized = cdf * float(hist.max()) / cdf.max()

    fig, ax1 = plt.subplots(figsize=(5, 3))
    
    ax1.fill_between(range(256), hist, color='#1f77b4', alpha=0.7) 
    ax1.plot(range(256), hist, color='darkblue', linewidth=0.5) # خط حدود خفيف
    
    ax1.set_xlim([0, 256])
    ax1.set_ylabel('# of pixels', fontsize=10)
    
    # الخط التراكمي
    ax2 = ax1.twinx()
    ax2.plot(cdf_normalized, color='blue', linewidth=2)
    ax2.set_yticks([]) 
    
    plt.title(title, fontsize=12)
    return fig

# --- Interface Streamlit ---
st.set_page_config(page_title="SIDI Medical Image Lab", layout="wide")
st.title("🔬 Amélioration d'Images Médicales (AI Powered)")

st.sidebar.header("⚙️ Configuration")
uploaded_file = st.sidebar.file_uploader("Charger une image (X-ray, IRM)", type=['png', 'jpg', 'jpeg'])

if uploaded_file is not None:
    file_bytes = np.asarray(bytearray(uploaded_file.read()), dtype=np.uint8)
    img_orig = cv2.imdecode(file_bytes, cv2.IMREAD_GRAYSCALE)

    auto_clip, auto_grid = get_auto_params(img_orig)
    st.sidebar.info(f"💡 Suggestion IA : Clip={auto_clip}, Grid={auto_grid}")

    st.sidebar.subheader("Paramètres CLAHE")
    clip_limit = st.sidebar.slider("Clip Limit", 1.0, 5.0, auto_clip)
    grid_size = st.sidebar.slider("Tile Grid Size", 4, 16, auto_grid)

    img_he = cv2.equalizeHist(img_orig)
    clahe_obj = cv2.createCLAHE(clipLimit=clip_limit, tileGridSize=(grid_size, grid_size))
    img_clahe = clahe_obj.apply(img_orig)

    # 
    mse_val, psnr_val, ssim_val = calculate_metrics(img_orig, img_clahe)

    # 
    st.divider()
    col1, col2, col3 = st.columns(3)
    with col1:
        st.subheader("Image Originale")
        st.image(img_orig, use_container_width=True)
    with col2:
        st.subheader("Égalisation (HE)")
        st.image(img_he, use_container_width=True)
    with col3:
        st.subheader("Résultat CLAHE")
        st.image(img_clahe, use_container_width=True)

    # 
    st.divider()
    st.subheader("📊 Évaluation Quantitative (Metrics)")
    m1, m2, m3 = st.columns(3)
    m1.metric("MSE (Erreur)", f"{mse_val:.2f}")
    m2.metric("PSNR (Qualité dB)", f"{psnr_val:.2f}")
    m3.metric("SSIM (Fidélité Structurelle)", f"{ssim_val:.4f}") # تم تصحيح المتغير إلى ssim_val
    
    st.caption("Note: SSIM proche de 1 signifie une préservation parfaite des structures anatomiques.")

    # hist
    st.divider()
    h_col1, h_col2, h_col3 = st.columns(3)
    with h_col1:
        st.pyplot(plot_styled_histogram(img_orig, "Histogramme Original"))
    with h_col2:
        st.pyplot(plot_styled_histogram(img_he, "Histogramme HE"))
    with h_col3:
        st.pyplot(plot_styled_histogram(img_clahe, "Histogramme CLAHE"))

    # زر التحميل
    is_success, buffer = cv2.imencode(".png", img_clahe)
    if is_success:
        st.sidebar.download_button("Télécharger l'image CLAHE", data=buffer.tobytes(), file_name="resultat_clahe.png")
else:
    st.info("Veuillez charger une image médicale pour commencer.")
