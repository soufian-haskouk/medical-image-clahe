\# 🔬 Medical Image Enhancement using CLAHE (Streamlit App)



Ce projet a été réalisé dans le cadre du Master SIDI (Systèmes d'Information Décisionnels et Imagerie) - Faculté des Sciences et Techniques Errachidia. Il implémente une application interactive pour l'amélioration du contraste des images médicales (Radiographies et IRM) en utilisant la technique \*\*CLAHE (Contrast Limited Adaptive Histogram Equalization)\*\* comparativement à l'égalisation globale (HE).



\---



\## 🚀 Fonctionnalités principales

\- \*\*Interface Interactive (Streamlit) :\*\* Permet de charger des images médicales et de régler dynamiquement les paramètres.

\- \*\*Suggestion Intelligente (Smart CLAHE) :\*\* Analyse automatique de l'écart-type de l'image pour proposer les meilleurs paramètres de \*Clip Limit\* et \*Tile Grid Size\*.

\- \*\*Évaluation Quantitative :\*\* Calcul en temps réel de trois métriques clés de qualité d'image :

&#x20; - \*\*MSE\*\* (Erreur Quadratique Moyenne)

&#x20; - \*\*PSNR\*\* (Rapport Signal sur Bruit de Crête)

&#x20; - \*\*SSIM\*\* (Fidnalité/Similarité Structurelle)

\- \*\*Visualisation Avancée :\*\* Affichage des histogrammes de distribution des pixels superposés avec la fonction de distribution cumulative (CDF).

\- \*\*Exportation :\*\* Téléchargement direct de l'image traitée.



\---



\## 🛠️ Technologies Utilisées

\- \*\*Python\*\*

\- \*\*OpenCV (`cv2`)\*\* : Traitement d'images et application CLAHE/HE.

\- \*\*Streamlit\*\* : Création de l'interface web.

\- \*\*NumPy \& Matplotlib\*\* : Calculs statistiques et génération des graphiques.

\- \*\*scikit-image\*\* : Calcul du score SSIM.



\---



\## ⚙️ Installation et Exécution



1\. Clonez le dépôt :

&#x20;  ```bash

&#x20;  git clone \[https://github.com/soufian-haskouk/medical-image-clahe.git](https://github.com/soufian-haskouk/medical-image-clahe.git)

&#x20;  cd medical-image-clahe

