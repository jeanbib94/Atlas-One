#programme qui calcule le temps nécessaire pour parcourir une distance.
distance_a_parcourir = float(input("Quelle distance doit parcourir le robot ?"))
vitesse_souhaitee = float(input("Quelle vitesse souhaitez-vous pour le robot ?"))
temps = distance_a_parcourir/vitesse_souhaitee
print(f"Le temps estimé est de {temps : .2f} s")