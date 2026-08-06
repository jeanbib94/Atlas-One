robot_name = "Atlas One"
robot_speed = 12.5
robot_weight = 10
battery_level = 80
robot_status = True

print(f"""==========ROBOT================
Nom : {robot_name}
Vitesse: {robot_speed}
Niveau de batterie : {battery_level}
Etat : {robot_status}""")

#Distance parcourue par le robot
vitesse = 1.25
temps = 240
distance=vitesse*temps
print(f"La distance parcourue est {distance}m ")