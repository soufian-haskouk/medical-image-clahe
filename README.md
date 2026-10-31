![Status](https://img.shields.io/badge/Status-Completed-success)
![Version](https://img.shields.io/badge/Release-v1.0.0-blue)
![License](https://img.shields.io/badge/License-All_Rights_Reserved-red)
![PHP](https://img.shields.io/badge/PHP-8.2-777BB4?logo=php&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.x-3776AB?logo=python&logoColor=white)
![MySQL](https://img.shields.io/badge/MySQL-Database-4479A1?logo=mysql&logoColor=white)

# 🚗 <ins>AGHARAS — Plateforme Web de Covoiturage avec Système de Recommandation basé sur l'IA</ins>

<p align="center">
  <b>AGHARAS</b> est une plateforme web dynamique de covoiturage conçue et développée par <b>SOUFIAN-haskouk</b>.
</p>

---

## 📌 <ins>Présentation du Projet</ins>

Face aux défis croissants du transport urbain et interurbain *(embouteillages, coûts élevés des véhicules individuels, rareté des transports en commun)*, **AGHARAS** propose une solution numérique collaborative, sécurisée et intuitive[cite: 11]. La plateforme met en relation directe les conducteurs et les passagers pour partager les frais de trajet tout en réduisant l'empreinte écologique.

---

## 📸 <ins>Quelques Interfaces & Diagrammes (Screenshots)</ins>

### 🖥️ **Application Web & Espace Utilisateur**
| **Page d'Accueil** | **Inscription** | **Profil Utilisateur** |
| :---: | :---: | :---: |
| ![Accueil](forUs/screenshots/home.png) | ![Inscription](forUs/screenshots/inscription.png) | ![Profil](forUs/screenshots/Profile.png) |

| **Gestion des Trajets** | **Reçu de Réservation (PDF)** | **Espace Administrateur** |
| :---: | :---: | :---: |
| ![Trajets](forUs/screenshots/Trajet.png) | ![Reçu PDF](forUs/screenshots/recu.png) | ![Admin Dashboard](forUs/screenshots/espaceadministrateur.png) |

---

### 📊 **Modélisation UML & Planification**
| **Diagramme de Cas d'Utilisation (Use Case)** | **Diagramme de Séquence (Réservation)** | **Planning (Gantt)** |
| :---: | :---: | :---: |
| ![Use Case Diagram](forUs/screenshots/USECase.png) | ![Sequence Diagram](forUs/screenshots/Seq__Réserver.png) | ![Gantt Chart](forUs/screenshots/Gantt.png) |

---

## 🌟 <ins>Fonctionnalités Principales</ins>

### 👤 **1. Gestion des Utilisateurs & Sécurité**
* **Inscription & Authentification :** Création de comptes sécurisée *(Passager / Conducteur)* avec validation des mots de passe et protection anti-robot (`reCAPTCHA`).
* **Récupération de mot de passe :** Système de réinitialisation sécurisé par lien envoyé par e-mail.
* **Espace Personnel (Profil) :** Modification des informations personnelles et consultation des statistiques individuelles *(trajets proposés, passagers transportés, note moyenne)*.

### 🚗 **2. Gestion des Trajets**
* **Publication d'annonces :** Les conducteurs peuvent publier facilement leurs trajets avec définition des points de départ, d'arrivée, des horaires et des prix.
* **Recherche Avancée :** Filtrage intelligent des trajets selon la destination, la date et les préférences.
