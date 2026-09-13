#Inventaire des capteurs du robot 

#Gestion de l'inventaire des capteurs
def afficher_inventaire():
    print("Inventaire des capteurs du robot :")
    for capteur in capteurs:
        print("- " + capteur)   

def ajouter_capteur(nouveau_capteur):
    if nouveau_capteur not in capteurs:
        capteurs.append(nouveau_capteur)
        print(f"{nouveau_capteur} a été ajouté à l'inventaire.")
    else:
        print(f"{nouveau_capteur} est déjà présent dans l'inventaire.")

def supprimer_capteur(capteur_a_supprimer):
    if capteur_a_supprimer in capteurs:
        capteurs.remove(capteur_a_supprimer)
        print(f"{capteur_a_supprimer} a été supprimé de l'inventaire.")
    else:
        print(f"{capteur_a_supprimer} n'est pas présent dans l'inventaire.")

def nombre_de_capteurs():
    return len(capteurs)

#Programme principal
if __name__ == "__main__":
    capteurs = ["capteur_lidar","capteur_camera", "capteur_ultrason"]

    while True:
        print("\nMenu de gestion de l'inventaire des capteurs :")
        print("1. Afficher l'inventaire")
        print("2. Ajouter un capteur")
        print("3. Supprimer un capteur")
        print("4. Nombre de capteurs")
        print("5. Quitter")

        choix = input("Veuillez entrer votre choix (1-5) : ")

        if choix == "1":
            afficher_inventaire()
        elif choix == "2":
            nouveau_capteur = input("Entrez le nom du capteur à ajouter : ")
            ajouter_capteur(nouveau_capteur)
        elif choix == "3":
            capteur_a_supprimer = input("Entrez le nom du capteur à supprimer : ")
            supprimer_capteur(capteur_a_supprimer)
        elif choix == "4":
            print(f"Nombre de capteurs dans l'inventaire : {nombre_de_capteurs()}")
        elif choix == "5":
            print("Au revoir !")
            break
        else:
            print("Choix invalide, veuillez réessayer.")

    