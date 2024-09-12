# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

# Niveau de batterie du bateau
niveauBatterie = int(input("Pourcentage de la batterie : "))

# Entre 50% et 100% de batterie, chaque pourcentage équivaut à 2km.
distCinquante_cent = 2
# Entre 25% et 50% de batterie, chaque pourcentage équivaut à 0,5km
distVingtCinq_cinquante = 0.5
# Entre 10% et 25% de batterie, chaque pourcentage équivaut à 1km
distDix_vingtCinq = 1
# Entre 5% et 10% de batterie, chaque pourcentage équivaut à 2.5km
distCinq_dix = 2.5
# Entre 0% et 5% de batterie, chaque pourcentage équivaut à 6km
distZero_cinq = 6

dist = 0
# L'utilisateur devra entrer son niveau de batterie tant qu'il est supérieur à 100% et inférieur à 0%
while (niveauBatterie < 0 or niveauBatterie > 100) :
    print("Erreur : Le niveau de batterie doit être entre 0 et 100 pour-cent.")
    niveauBatterie = int(input("Pourcentage de la batterie : "))

def determinerDistance(niveauBatterie) :
    if 50 < niveauBatterie <= 100 :
        dist = niveauBatterie * distCinquante_cent
    elif 25 < niveauBatterie <= 50 :
        dist = niveauBatterie * distVingtCinq_cinquante
    elif 10 < niveauBatterie <= 25 :
        dist = niveauBatterie * distDix_vingtCinq
    elif 5 < niveauBatterie <= 10 :
        dist = niveauBatterie * distCinq_dix
    elif 0 < niveauBatterie <= 5 :
        dist = niveauBatterie * distZero_cinq
    
    return dist

exit = f"La distance possible est de {determinerDistance(niveauBatterie)} km."
print(exit)