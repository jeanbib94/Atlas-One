#Fonction permettant de calculer l'autonomie d'un robot
def calculer_autonomie(batterie, consommation):
    """
    Calcule l'autonomie restante en heures.
    batterie : capacité disponible en mAh ou Wh
    consommation : consommation en mA ou W par heure
    """
    if consommation <= 0:
        return 0
    
    # Temps restant en heures
    temps_restant = batterie / consommation
    return temps_restant


# 2. Programme principal qui gère la saisie et les différents robots
if __name__ == "__main__":
    print("=== ASSISTANT D'AUTONOMIE DES ROBOTS ===")
    
    # On peut créer une boucle pour tester plusieurs robots
    nombre_robots = int(input("Combien de robots voulez-vous analyser ? "))
    
    for i in range(1, nombre_robots + 1):
        print(f"\n--- Robot n°{i} ---")
        
        # Demande des données
        capacite = float(input("Capacité utile de la batterie (en mAh) : "))
        niveau = float(input("Niveau actuel (%) : "))
        consommation = float(input("Consommation moyenne (en mA) : "))
        
        # Calcul de la batterie réelle disponible
        batterie_disponible = capacite * (niveau / 100)
        
        # Appel de la fonction
        autonomie_h = calculer_autonomie(batterie_disponible, consommation)
        autonomie_min = autonomie_h * 60
        
        # Affichage du résultat
        print(f"⏱️ Autonomie restante pour Robot {i} : {autonomie_h:.2f} h ({autonomie_min:.0f} min)")