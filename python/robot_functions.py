#==========Definition des fonctions pour le robot==========
def initialisation_robot():
    print("Initialisation du robot...")

def afficher_etat_robot(battery, temperature, distance_obstacle):
    print("-----------------------------")
    print("État actuel du robot:")
    print(f"Niveau de batterie: {battery}%")
    print(f"Température ambiante: {temperature}°C")
    print(f"Distance à l'obstacle le plus proche: {distance_obstacle} cm")
    print("-----------------------------")

def calculer_distance():
    vitesse = float(input("Entrez la vitesse du robot (en m/s): "))
    temps = float(input("Entrez le temps de déplacement (en s): "))
    distance = vitesse * temps
    print(f"Distance parcourue: {distance} m")

def arreter_robot():
    print("Arrêt du robot.")

#==========Programme principal==========
if __name__ == "__main__":
    initialisation_robot()
    battery = float(input("Entrez le niveau de batterie du robot (0-100): "))
    temperature = float(input("Entrez la température ambiante (en °C): "))
    distance_obstacle = float(input("Entrez la distance à l'obstacle le plus proche (en cm): "))

    afficher_etat_robot(battery, temperature, distance_obstacle)

    if battery < 10 or temperature > 70 or distance_obstacle < 20:
        print("Arrêt d'urgence.")
        arreter_robot()
    else:
        alerte = False
        if battery < 20:
            print("Alerte: Niveau de batterie faible.")
            alerte = True
        if distance_obstacle < 50:
            print("Alerte: Obstacle détecté.")
            alerte = True
        if not alerte:
            print("Mission autorisée.")

        calculer_distance()

        arreter_robot()
    