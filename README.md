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