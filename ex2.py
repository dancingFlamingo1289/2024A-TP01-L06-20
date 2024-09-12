# TODO: Créer un script pour calculer les ressources nécessaires pour assainir la Seine.
# TODO: Importer les modules nécessaires.
import math

# Quantité d'eau de base à assanir.
qteEauBase = 5
# Quantité de filtres pour assanir qteEauBase d'eau
qteFiltresRequise = 1
# Quantité de lampes pour assanir qteEauBase d'eau
qteLampesRequise = 3
# Quantité de chlore (en kilogrammes) pour assanir qteEauBase d'eau
qteChloreRequise = 0.5

qteEauStr = input("Quelle quantité d'eau faut-il assanir ? ")

if (qteEauStr != "") :
    qteEau = float(qteEauStr)

    rapportEau = qteEau / qteEauBase

    qteFiltres = qteFiltresRequise * rapportEau
    qteLampes = qteLampesRequise * rapportEau
    qteChlore = qteChloreRequise * rapportEau

    sortie = (f"Voici les elements requis pour assainir {qteEau}L d'eau:\n\n" +
                f"\t- Filtre(s) : {qteFiltres}\n\n" +
                f"\t- Lampes UV : {qteLampes}\n\n" +
                f"\t- Chlore : {qteChlore}kg\n\n")
    print(sortie)