# TODO: Écrire un programme qui demande le pourcentage de charge actuel de la batterie du bateau,
#        calcule la distance restante en km en fonction de ce pourcentage,
#        et affiche le résultat au format "XX km".
#        Assurez une gestion du pourcentage valide au cours de votre programme (% toujours dans [0 ; 100]).

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
#while (niveauBatterie < 0 or niveauBatterie > 100) :
    #print("Erreur : Le niveau de batterie doit être entre 0 et 100 pour-cent.")
    #niveauBatterie = int(input("Pourcentage de la batterie : "))

def determinerDistance(niveauBatterie) :
    dist = 0.0
    bornes = [100, 50, 25, 10, 5, 0]

    if niveauBatterie > bornes[1] :
        dist += (niveauBatterie - bornes[1]) * distCinquante_cent
        niveauBatterie = bornes[1]

    if niveauBatterie > bornes[2] :
        dist += (niveauBatterie - bornes[2]) * distVingtCinq_cinquante
        niveauBatterie = bornes[2]

    if niveauBatterie > bornes[3] :
        dist += (niveauBatterie - bornes[3]) * distDix_vingtCinq
        niveauBatterie = bornes[3]

    if niveauBatterie > bornes[4] :
        dist += (niveauBatterie - bornes[4]) * distCinq_dix
        niveauBatterie = bornes[4]

    if niveauBatterie > bornes[5] :
        dist += (niveauBatterie - bornes[5]) * distZero_cinq
        niveauBatterie = bornes[5]
    
    return dist

# Niveau de batterie du bateau
niveauBatterie = float(input("Pourcentage de batterie ? "))

exit = ""
if niveauBatterie == 0 :
    exit = "La batterie est vide"
else :
    dist = round(determinerDistance(niveauBatterie), 1)
    exit = f"{dist} km"

print(exit)