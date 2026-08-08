#Prise decision pour le robot
battery = float(input("Entrez le niveau de batterie du robot (0-100):"))
temperature = float(input("Entrez la température ambiante (en °C): "))
distance_obstacle = float(input("Entrez la distance à l'obstacle le plus proche (en cm): "))

if battery < 10 or temperature > 70 or distance_obstacle < 20:
    print("Arrêt d'urgence.")
else : 
    if battery < 20:
        print("Alerte: Niveau de batterie faible.")
    if distance_obstacle < 50:
        print("Alerte: Obstacle détecté.")
    else:
        print("Mission autorisée.")