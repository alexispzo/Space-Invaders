#------------------------------------------------------------------------------------------------------------------
# Auteurs : BEN AMMAR Kenzi - BALLAND ALEXIS
# Date de réalisation : 17 Decembre 2023
# Objectifs de la classe Alien :
#   Cette classe représente un alien dans le contexte d'une application graphique utilisant Tkinter.
#   Elle est responsable de l'initialisation des propriétés de l'alien, de la mise à jour de sa position,
#   de la gestion des projectiles tirés par l'alien, de la vérification des collisions avec le canvas 
#   pour changer sa direction, et du rendu graphique de l'alien et de ses projectiles sur le canevas.
#
#   Méthodes principales :
#   - __init__ :
#       - But : Créer une instance d'alien avec une position initiale, une image spécifiée, et un 
#         éventuel redimensionnement.
#       - Entrées :
#           - x (int): La position horizontale initiale de l'alien.
#           - y (int): La position verticale initiale de l'alien.
#           - image_path (str): Le chemin vers le fichier image représentant l'alien. 
#           - resize (int): Le facteur de redimensionnement de l'image. 
#       - Sorties : Aucune.
#
#   - update :
#       - But : Actualiser la position de l'alien et déclencher le tir de projectiles.
#       - Méthode : Incrémente la position horizontale de l'alien et déclenche la méthode tirer
#         pour lancer des projectiles à une certaine probabilité.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - tirer :
#       - But : Créer un projectile avec une probabilité d'environ 0.1%.
#       - Méthode : Génère un projectile à partir de la position de l'alien avec une probabilité
#         d'environ 0.1% et l'ajoute à la liste des projectiles.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - check_collision :
#       - But : Vérifier si l'alien a atteint les bords gauche ou droit du canevas et ajuster 
#         sa direction si nécessaire.
#       - Méthode : Vérifie si l'alien a atteint les bords gauche ou droit du canevas et ajuste
#         sa direction en conséquence.
#       - Entrées : Aucune.
#       - Sorties :
#           - collision (bool): True si une collision est détectée, False sinon.
#
#   - draw :
#       - But : Afficher graphiquement l'alien et ses projectiles sur le canevas.
#       - Méthode : Dessine l'image de l'alien sur le canevas à sa position actuelle et appelle la
#         méthode draw de chaque projectile associé pour les afficher également.
#       - Entrées :
#           - canvas (Tkinter Canvas): L'objet Canvas sur lequel dessiner l'alien et les projectiles.
#       - Sorties : Aucune.
#--------------------------------------------------------------------------------------------------------------------


import random
from tkinter import PhotoImage
from Projectile import Projectile

class Alien:
     def __init__(self, x, y, image_path="image/alien.png", resize=8):
        self.x = x
        self.y = y
        self.direction = 1  
        self.projectiles = []
        image = PhotoImage(file=image_path)
        self.image = image.subsample(resize, resize)


     def update(self):
        self.x += self.direction * 1.5  
        self.tirer()
    

     def tirer(self):
        if random.random() <= 0.001:
               projectile = Projectile(self.x + 15, self.y + 30, vitesse=3)
               self.projectiles.append(projectile)


     def check_collision(self):
        return self.x <= 18 or self.x >= 785


     def draw(self, canvas):
        canvas.create_image(self.x , self.y, image=self.image)
        
        for projectile in self.projectiles:
            projectile.draw(canvas)




