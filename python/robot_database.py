#Base de données des robots de Atlas-One

robot1 = {
    "Nom": "Atlas-One",
    "Batterie": 80,
    "Vitesse": 1.5,
    "Température": 25,
}
robot2 = {
   "Nom": "Atlas-Two",
       "Batterie": 70,
       "Vitesse": 1.2,
       "Température": 26,
}
robot3 = {
    "Nom": "Atlas-Three",
    "Batterie": 60,
    "Vitesse": 1.0,
    "Température": 27,
}   

robots = [ robot1, robot2, robot3 ] 

print("=== Informations sur les robots ===")
for robot in robots:
    print(f"Robot : {robot['Nom']}")
    print(f"Etat : {robot['Température']} °C,  {robot['Vitesse']} m/s")
    print(f"Batterie : {robot['Batterie']}mAh")
   
#print(robots)
#print(robot2)
#print(robot3)   