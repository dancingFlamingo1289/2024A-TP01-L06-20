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

qteEau = float(input("Quelle quantité d'eau faut-il assanir ? "))
rapportEau = qteEau // qteEauBase

qteFiltres = qteFiltresRequise * rapportEau
qteLampes = qteLampesRequise * rapportEau
qteChlore = qteChloreRequise * rapportEau

print("Bonjour"*20)

sortie = (f"Voici les matériaux requis pour l'assainissement de {qteEau} L d'eau :\n" +
          f"\t- {qteFiltres} filtres\n" + 
          f"\t- {qteLampes} lampes UV\n" +
          f"\t- {qteChlore} kg de chlore")
print(sortie)