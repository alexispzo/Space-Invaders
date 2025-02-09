#------------------------------------------------------------------------------------------------------------------
# Auteurs : BEN AMMAR Kenzi - BALLAND ALEXIS
# Date de réalisation : 17 Decembre 2023
# Objectifs de la classe Projectile :
#   Cette classe représente un projectile dans le contexte d'une application graphique utilisant Tkinter.
#   Elle est responsable de l'initialisation des propriétés du projectile, de la mise à jour de sa 
#   position, de la vérification s'il est hors de l'écran, et du rendu graphique du projectile sur 
#   le canevas.
#
#   Méthodes principales :
#   - __init__ :
#       - But : Créer une instance de projectile avec une position initiale et une vitesse spécifiées.
#       - Entrées :
#           - x (int): La position horizontale initiale du projectile.
#           - y (int): La position verticale initiale du projectile.
#           - vitesse (int): La vitesse du projectile. Par défaut : 3.
#       - Sorties : Aucune.
#
#   - update :
#       - But : Actualiser la position du projectile en fonction de sa vitesse.
#       - Méthode : Incrémente la position verticale du projectile en fonction de sa vitesse.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - is_offscreen :
#       - But : Vérifier si le projectile est hors de l'écran.
#       - Méthode : Vérifie si la position verticale du projectile est hors des limites de l'écran.
#       - Sorties :
#           - hors_ecran (bool): True si le projectile est hors de l'écran, False sinon.
#  
#   - draw :
#       - But : Afficher graphiquement le projectile sur le canevas.
#       - Méthode : Dessine un rectangle sur le canevas représentant le projectile à sa position actuelle.
#       - Entrées :
#           - canvas (Tkinter Canvas): L'objet Canvas sur lequel dessiner le projectile.
#       - Sorties : Aucune.
#--------------------------------------------------------------------------------------------------------------------


class Projectile:
    def __init__(self, x, y, vitesse=3):
        self.x = x
        self.y = y
        self.vitesse = vitesse  


    def update(self):
        self.y += self.vitesse 


    def is_offscreen(self):
        return self.y < 0 or self.y > 600


    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y, self.x + 5, self.y + 10, fill="red")