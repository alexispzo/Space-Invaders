#------------------------------------------------------------------------------------------------------------------
# Auteurs : BEN AMMAR Kenzi - BALLAND ALEXIS
# Date de réalisation : 17 Decembre 2023
# Objectifs de la classe Vaisseau :
#   Cette classe représente un vaisseau spatial dans le contexte d'une application graphique utilisant 
#   Tkinter. Elle est responsable de l'initialisation des propriétés du vaisseau, de la mise à jour 
#   de sa position, du déplacement, de la gestion de la vie, du tir de projectiles, et du rendu 
#   graphique du vaisseau et de ses projectiles sur le canevas.
#
#   Méthodes principales :
#   - __init__ :
#       - But : Créer une instance de vaisseau avec une position initiale, une image spécifiée, et un
#         éventuel redimensionnement.
#       - Entrées :
#           - image_path (str): Le chemin vers le fichier image représentant le vaisseau.
#           - resize (int): Le facteur de redimensionnement de l'image. Par défaut : 10.
#       - Sorties : Aucune.
#
#   - update :
#       - But : Mettre à jour la position du vaisseau et des projectiles associés.
#       - Méthode : Appelle la méthode update de chaque projectile associé et retire les projectiles 
#                   hors de l'écran.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - deplacement_droite :
#       - But : Déplacer le vaisseau vers la droite, si possible.
#       - Méthode : Modifie la position horizontale du vaisseau.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - deplacement_gauche :
#       - But : Déplacer le vaisseau vers la gauche, si possible.
#       - Méthode : Modifie la position horizontale du vaisseau.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - tirer :
#       - But : Créer un projectile associé au vaisseau et l'ajouter à la liste des projectiles.
#       - Méthode : Crée un projectile au-dessus du vaisseau avec une vitesse vers le haut et 
#                   l'ajoute à la liste.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - draw :
#       - But : Afficher graphiquement le vaisseau et ses projectiles sur le canevas.
#       - Méthode : Utilise la méthode create_image de Tkinter pour afficher le vaisseau et appelle 
#                   la méthode draw de chaque projectile associé.
#       - Entrées :
#           - canvas (Tkinter Canvas): L'objet Canvas sur lequel dessiner le vaisseau et les projectiles.
#       - Sorties : Aucune.
#
#   - perte_vie :
#       - But : Réduire la vie du vaisseau lorsqu'il est touché.
#       - Méthode : Décrémente la vie du vaisseau.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#--------------------------------------------------------------------------------------------------------------------

from tkinter import PhotoImage
from Projectile import *

class Vaisseau:
    def __init__(self,image_path="image/vaisseau.png", resize=10) :
        self.x = 400
        self.y = 550
        self.vie = 3
        self.projectiles = []
        image=PhotoImage(file=image_path)
        self.image = image.subsample(resize, resize)


    def update(self):
        for projectile in self.projectiles:
            projectile.update()
        
        self.projectiles = [projectile for projectile in self.projectiles if not projectile.is_offscreen()]


    def deplacement_droite(self):
        if self.x < 720 :
            self.x += 20


    def deplacement_gauche(self):
        if self.x > 0 :
            self.x -= 20
        

    def tirer(self):
        projectile = Projectile(self.x -5 , self.y -40, vitesse=-3)
        self.projectiles.append(projectile)


    def draw(self,canvas):
        canvas.create_image(self.x , self.y, image=self.image)
        
        for projectile in self.projectiles:
            projectile.draw(canvas)  


    def perte_vie(self):
        self.vie -= 1 

