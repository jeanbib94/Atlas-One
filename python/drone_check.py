#Assistant de decollage pour un drône
battery_min = 70        #% de batterie
vitesse_vent_max = 30   #km/h

battery = float(input("Entrez le niveau de batterie du drone (0-100): "))
vitesse_vent = float(input("Entrez la vitesse du vent (en km/h): "))
gps_disponible = input("Le GPS est-il disponible ? (oui/non): ").strip().lower()   
gps = False 

if gps_disponible == "oui":
    gps = True

if battery < battery_min or vitesse_vent > vitesse_vent_max or not gps:
    print("Décollage interdit.")
else:
    print("Décollage autorisé.")