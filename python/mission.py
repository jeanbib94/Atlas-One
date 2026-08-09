#==========Definition des fonctions pour la mission du robot==========
def verifier_batterie(batterie):
    if batterie < 20:
        print("Niveau de batterie critique. Le robot ne peut pas effectuer la mission. Rechargez le robot.")
    elif batterie < 50:
        print("Alerte: Niveau de batterie faible.")
    else:
        print("Niveau de batterie suffisant pour la mission.")

def detecter_obstacle(distance_obstacle):
    if distance_obstacle < 20:
        print("Obstacle très proche. Arrêt d'urgence.")
    elif distance_obstacle < 50:
        print("Alerte: Obstacle détecté.")
    else:
        print("Pas d'obstacle à proximité.")

def calculer_vitesse():
    distance = float(input("Entrez la distance à parcourir par le robot (en mètres): "))
    temps = float(input("Entrez le temps pour parcourir cette distance (en secondes): "))

    if temps <= 0:
        print("Le temps doit être supérieur à 0.")
        return 0
    
    vitesse = distance / temps
    print(f"La vitesse du robot sera de : {vitesse:.2f} m/s")

def afficher_etat_robot(batterie, temperature, distance_obstacle):
    print(f"----État du robot----")
    print(f"Niveau de batterie: {batterie}%")
    print(f"Température ambiante: {temperature}°C")
    print(f"Distance à l'obstacle le plus proche: {distance_obstacle} cm")
    print("---------------------")

def demarrer_mission():
    print("Mission démarrée ! Le robot effectue son trajet...")

def arreter_mission():
    print("Fin de mission.")
    

#==========Programme principal==========
batterie = float(input("Entrez le niveau de batterie du robot (0-100): "))
distance_obstacle = float(input("Entrez la distance à l'obstacle le plus proche (en cm): "))
temperature = float(input("Entrez la température ambiante (en °C): "))

print("\n--- Phase de contrôle ---")
verifier_batterie(batterie)
detecter_obstacle(distance_obstacle)

#Verification globale des conditions pour démarrer la mission
if batterie < 20 or temperature > 70 or distance_obstacle < 20:
    print("\nConditions critiques : Mission annulée !")
    arreter_mission()
else:
    afficher_etat_robot(batterie, temperature, distance_obstacle)
    calculer_vitesse()
    demarrer_mission()
    arreter_mission()




