# 🔬 Amélioration d'Images Médicales par la Technique CLAHE

> **Application Interactive sous Python & Streamlit avec Évaluation Quantitative (MSE, PSNR, SSIM)**

---

## 📌 Présentation 

Il explore et démontre l'efficacité de la technique **CLAHE** (*Contrast Limited Adaptive Histogram Equalization*) par rapport à l'égalisation d'histogramme classique (HE) pour le rehaussement des radiographies et des IRM, tout en intégrant une **suggestion automatique intelligente (Smart CLAHE)** basée sur l'analyse statistique de l'image.

---

## 🌟 Fonctionnalités Principales

* **🖥️ Interface Web Interactive (Streamlit) :** Permet de charger facilement une image médicale (X-ray, IRM) et de régler dynamiquement les paramètres en temps réel.
* **💡 Suggestion Intelligente (IA) :** Analyse automatique de l'écart-type de l'image pour proposer les valeurs idéales de *Clip Limit* et de *Tile Grid Size*.
* **📊 Évaluation Quantitative Avancée :** Calcul instantané de trois métriques clés de qualité :
  * **MSE** (Erreur Quadratique Moyenne)
  * **PSNR** (Rapport Signal sur Bruit de Crête en dB)
  * **SSIM** (Fidélité et Similarité Structurelle)
* **📈 Visualisation Graphique :** Affichage des histogrammes de distribution des pixels avec superposition de la courbe cumulative (CDF).
* **💾 Exportation du Résultat :** Téléchargement direct de l'image traitée au format PNG.

---

## 🛠️ Technologies & Bibliothèques Utilisées

| Technologie / Librairie | Rôle Principal |
| :--- | :--- |
| **Python** | Langage de programmation principal |
| **Streamlit** | Création de l'interface utilisateur web |
| **OpenCV (`cv2`)** | Traitement d'images, application des filtres HE et CLAHE |
| **NumPy & Matplotlib** | Calculs numériques, statistiques et tracés des histogrammes |
| **scikit-image** | Calcul précis du score de similarité structurelle (SSIM) |

---

## ⚙️ Installation et Exécution Locale

Suivez ces étapes pour lancer l'application sur votre machine :

1. **Cloner le dépôt ou placer les fichiers dans un dossier :**
   ```bash
   cd medical-image-clahe
