# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
from math import ceil
# Quantité d'eau de base à assanir.
qteEauBase = 5
# Quantité de filtres pour assanir qteEauBase d'eau
qteFiltresRequise = 1
# Quantité de lampes pour assanir qteEauBase d'eau
qteLampesRequise = 3
# Quantité de chlore (en kilogrammes) pour assanir qteEauBase d'eau
qteChloreRequise = 0.5

qteEau = (input("Quelle quantité d'eau faut-il assainir ? "))

rapportEau = float(qteEau) / float(qteEauBase)

qteFiltres = float(qteFiltresRequise) * float(rapportEau)
qteLampes = float(qteLampesRequise) * float(rapportEau)
qteChlore = float(qteChloreRequise) * float(rapportEau)

qteFlitres = int(ceil(qteFiltres))
qteLampes = int(ceil(qteLampes))
qteChlore = float(qteChlore)

sortie = f"""Voici les éléments requis pour assainir {qteEau}L d'eau:\n\n        \t- Filtre(s) : {qteFlitres}\n\n        \t- Lampe(s) UV : {qteLampes}\n\n        \t- Chlore : {qteChlore}kg"""
print(sortie)