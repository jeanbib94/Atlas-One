# Atlas-One
# 🤖 Atlas-One : Robot Mobile Autonome

[![ROS 2](https://img.shields.io/badge/ROS2-Humble%20%2F%20Jazzy-blue?logo=ros)](https://docs.ros.org/)
[![Python](https://img.shields.io/badge/Python-3.10%2B-green?logo=python)](https://www.python.org/)
[![C++](https://img.shields.io/badge/C%2B%2B-17-blue?logo=cplusplus)](https://isocpp.org/)
[![Docker](https://img.shields.io/badge/Docker-Supported-blue?logo=docker)](https://www.docker.com/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

**Atlas-One** est un projet d'ingénierie complet développé dans le cadre d'un **Master Robotique & IA en autodidacte**. Ce projet fil rouge a pour but de concevoir, simuler et déployer un système robotique mobile autonome capable de cartographier son environnement, de naviguer en toute sécurité et d'interagir intelligemment avec son milieu via des algorithmes de Computer Vision et de Deep Learning.

---

## 🎯 Objectifs

- **Navigation Autonome & SLAM** : Cartographie en temps réel et planification de trajectoire optimale dans un environnement dynamique.
- **Vision par Ordinateur & IA** : Détection et suivi d'objets, reconnaissance d'obstacles complexes et interprétation de l'environnement via Deep Learning.
- **Architecture Logicielle Modulaire** : Découpage propre sous forme de nœuds ROS 2 pour garantir la scalabilité et le temps réel.
- **Simulation à Haute Fidélité** : Modélisation physique du robot dans Gazebo / Isaac Sim avant déploiement sur matériel réel.
- **Conteneurisation & MLOps** : Reproductibilité complète de l'environnement de développement et de déploiement via Docker.

---

## ⚡ Fonctionnalités

- 🗺️ **Cartographie SLAM 2D/3D** : Génération de cartes d'occupations via LiDAR et centrales inertielles (IMU).
- 📍 **Localisation & Path Planning** : Algorithmes A*, Dijkstra et TEB Local Planner via la stack **Nav2**.
- 👁️ **Perception Multimodale** : Fusion de données capteurs (Caméra RGB-D + LiDAR) pour la détection temps réel d'objets (YOLO / PyTorch).
- 🎮 **Contrôle à distance & Téléopération** : Interface de commande via nœuds clavier/manette et visualisation RViz2.
- 🐳 **Environnement Isolé** : Déploiement instantané de la stack complète dans un conteneur Docker préconfiguré.

---

## 🛠️ Technologies Utilisées

| Domaine | Technologies |
| :--- | :--- |
| **Middlewares & OS** | ROS 2 (Humble/Jazzy), Ubuntu Linux, RTOS |
| **Langages** | C++ (17/20), Python 3.10+, Bash |
| **Perception & IA** | OpenCV, PyTorch, YOLOv8, TensorRT |
| **Simulation & Outils** | Gazebo, RViz2, Webots |
| **DevOps & Outils** | Docker, Git, VS Code, CMake |

---

## 📸 Captures d'écran & Démonstrations

*(Ajoutez vos visuels et GIF animés dans le dossier `images/` et `videos/`)*

| Cartographie SLAM (RViz2) | Simulation Gazebo | Détection d'objets (YOLO) |
| :---: | :---: | :---: |
| ![SLAM RViz](images/.gitkeep) | ![Simulation Gazebo](images/.gitkeep) | ![YOLO Detection](images/.gitkeep) |
| *Visualisation des cartes et trajectoires* | *Environnement virtuel et modèle URDF* | *Flux vidéo et détection temps réel* |

---

## 📦 Installation

### Prérequis
- **Ubuntu 22.04 LTS** (ou supérieur)
- **Git**
- **Docker** et **Docker Compose** (Recommandé) ou **ROS 2 Humble** installé en local.

### Option A : Déploiement rapide via Docker (Recommandé)

1. **Cloner le dépôt** :
   ```bash
   git clone [https://github.com/jeanbib94/Atlas-One.git](https://github.com/jeanbib94/Atlas-One.git)
   cd Atlas-One


## 🗺️ Roadmap du Projet

| Phase | Objectif |
| :---: | :--- |
| **0** | **Environnement** (Linux, Git, VS Code, Docker) |
| **1** | **Python & C++** (Bases orientées objet, gestion mémoire) |
| **2** | **Linux** (Ligne de commande, gestion des processus, permissions) |
| **3** | **ROS 2** (Nodes, Topics, Services, Actions, Colcon) |
| **4** | **Robot Mobile** (Modélisation URDF, simulation Gazebo) |
| **5** | **Vision** (OpenCV, traitement d'image, caméras RGB-D) |
| **6** | **IA** (PyTorch, détection d'objets YOLO, classification) |
| **7** | **Navigation** (SLAM, cartographie, Nav2, planification de trajectoire) |
| **8** | **Manipulation** (Bras robotique, MoveIt 2, cinématique) |
| **9** | **Projet Final** (Intégration complète Hardware-in-the-Loop) |


## 🛠️ Configuration de l'environnement

Afin de maintenir un environnement propre et isolé, le projet utilise un environnement virtuel Python.

bash
# Création de l'environnement virtuel
python3 -m venv .venv

# Activation de l'environnement virtuel
source .venv/bin/activate

🚀 Scripts disponibles
1. Présentation du Robot (python/presentation.py)
Affiche la carte d'identité du robot Atlas One, la version exacte de Python exécutée via le module platform et la date du jour.Bashpython3 python/presentation.py
2. Infos & Calcul de Distance (python/robot_info.py)Calcule la distance parcourue à partir de données physiques de vitesse ($1.25\text{ m/s}$) et de temps ($240\text{ s}$).Bashpython3 python/robot_info.py
3. Système de Prise de Décision (python/robot_decision.py)Évalue la sécurité du robot selon plusieurs paramètres (batterie, température, distance d'obstacle).Arrêt d'urgence prioritaire si les seuils critiques sont dépassés.Cumul des alertes secondaires si plusieurs avertissements sont levés simultanément.Bashpython3 python/robot_decision.py
4. Assistant de Décollage Drône (python/drone_check.py)Contrôle les conditions avant de passer en vol : vitesse du vent, batterie minimale et disponibilité du GPS.Convertit les réponses textuelles (oui/non) en valeurs booléennes (True/False).Bashpython3 python/drone_check.py
5. Patrouille & Gestion de Batterie (python/robot_patrol.py)Simule la mission de patrouille du robot à l'aide d'une boucle while.Consommation de $7\%$ de batterie par déplacement.Interruption automatique et retour à la station de recharge dès que le niveau repasse sous les $20\%$.Bashpython3 python/robot_patrol.py

<p align="center">
  <img src="assets/demo_robot_patrol.png" alt="Aperçu du script" width="600"/>
</p>