# 📓 Journal de Bord — Projet Atlas-One

Ce journal retrace mon apprentissage autodidacte en Robotique & IA, mes choix techniques, les bugs rencontrés et les solutions apportées.

---

## 📅 Semaine 1 : [Setup de l'environnement]
**05/08/2026** : Du 01/08/2026 au 05/08/2026

### 📚 1. Notions étudiées
- Initialisation et gestion des dépôts distants avec **Git & GitHub**.
- Structure basique d'un fichier **Dockerfile** sous Ubuntu 24.04 / 26.04.
- Bases de la compilation C++ avec `g++` et scripts Python d'entrée (`main.py`).

### ⚠️ 2. Difficultés rencontrées
- Conflit d'historiques distants lors du `git push` (`rejected - non-fast-forward`).
- Gestion de l'authentification GitHub (suppression des mots de passe classiques via terminal).

### 💡 3. Solutions trouvées
- Utilisation de `git pull origin main --rebase` pour aligner l'historique local avec GitHub sans casser les commits.
- Génération et configuration d'un **Personal Access Token (PAT)** GitHub avec les permissions `repo`.

### 🚀 4. Pistes d'amélioration / Prochaines étapes
- [ ] Configurer un fichier `.gitignore` propre pour ignorer les exécutables C++ (ex: `atlas`).
- [ ] Passer à la modélisation URDF du robot dans Gazebo pour la semaine 2.

---

## 📅 Semaine 2 : [Python pour la robotique]

### 🚀 Évolution du projet Atlas-One

#### 🔧 Environnement & Outillage
- **Environnement virtuel (`.venv`)** : Mise en place et gestion de l'isolation des paquetages Python.
- **Versionnement Git** : Pratique régulière du cycle d'intégration (`git add`, `git commit -m "..."`, `git push`) pour garder une trace propre de l'historique sur GitHub.
- **Secrets & Configuration** : Exclusions des fichiers temporaires et des environnements virtuels via `.gitignore`.

#### 🐍 Compétences Python développées

1. **Variables & Calculs** :
   - Manipulation des types standards (`float`, `int`, `str`, `bool`).
   - Correction des syntaxes spécifiques à Python (utilisation du point `.` pour les décimaux, absence de mot-clé de type lors des déclarations).
   - Formules physiques de base ($\text{distance} = \text{vitesse} \times \text{temps}$).

2. **Structures conditionnelles avancées** :
   - Compréhension de l'exclusivité des blocs `if / elif / else`.
   - Utilisation de plusieurs blocs `if` indépendants pour permettre le **cumul des alertes**.
   - Priorisation des règles métier (arrêt d'urgence placé en premier).

3. **Interactions & Logique Booléenne** :
   - Nettoyage des saisies utilisateur avec `.strip().lower()`.
   - Conversion de réponses textuelles (`"oui"`, `"non"`) en booléens natifs (`True`, `False`) avec l'opérateur `in`.

4. **Boucles d'itération (`while`)** :
   - Implémentation d'une boucle conditionnelle contrôlant l'état d'un système (décharge de la batterie du robot).
   - Mise en place d'un compteur de boucle (`deplacement += 1`) et de décrémentation (`battery_level -= 7`).

5. **Formatage & Modules systèmes** :
   - Affichage dynamique des chaînes de caractères avec les f-strings (`f"..."`).
   - Importation et utilisation des modules natifs `datetime`, `timedelta` et `platform`