#Programme simulant une mission pour un robot en fonction de son niveau de batterie.
battery_limit = 20
battery_level = 100
deplacement = 0
while battery_level > battery_limit:
    deplacement += 1
    battery_level -= 7
    print(f"Déplacement {deplacement}: Niveau de batterie: {battery_level}%")
print("Retour à la station de recharge.")