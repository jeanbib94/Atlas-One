#Affiche le niveau de batterie
for i in range(100, 4, -5):
    print(f"Niveau de batterie: {i}%")
    if i <= 5:
        print("Recharge nécessaire!")