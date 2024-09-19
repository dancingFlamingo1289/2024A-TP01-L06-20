# TODO: Calculer la distance qu'un poids peut atteindre en utilisant la formule de la portée d'un projectile.
# TODO: Importer les modules nécessaires.
from math import sin, radians
#from scipy import constants
#$$D = \frac{vitesse^2 \times \sin(2 \times angle)}{g}$$

speed = float(input("Vitesse initiale (m/s): "))
angle = float(input("Angle de lancer (en degrés): "))

angle = radians(angle)

def calcul_distance(speed, angle):
    return (speed**2 * sin(2 * angle))/round(9.81, 1)
    
D = calcul_distance(speed, angle)

print(f"Distance parcourue: {round(D, 2)}m")