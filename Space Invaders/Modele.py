#------------------------------------------------------------------------------------------------------------------
# Auteurs : BEN AMMAR Kenzi - BALLAND ALEXIS
# Date de réalisation : 17 Decembre 2023
# Objectifs de la classe Modele :
#   Cette classe agit en tant que modèle dans une application graphique utilisant Tkinter. Elle est responsable
#   de la gestion de l'état du jeu, des éléments graphiques tels que le vaisseau, les aliens, les protections,
#   et des interactions entre eux. Elle implémente également la logique du jeu, notamment la mise à jour des 
#   positions des éléments, la détection de collisions et la gestion du score.
#
#   Méthodes principales :
#   - __init__ :
#       - But : Initialiser une instance de Modele avec les éléments principaux.
#       - Entrées :
#           - fenetre (Tkinter Tk): L'objet principal de la fenêtre Tkinter.
#       - Sorties : Aucune.
#
#   - create_aliens :
#       - But : Créer une grille d'aliens initiale avec une disposition spécifiée.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - create_protections :
#       - But : Créer une rangée de protections initiales.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - update_alien_projectiles :
#       - But : Mettre à jour la position des projectiles tirés par les aliens.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - move_aliens_down :
#       - But : Déplacer tous les aliens vers le bas.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - update :
#       - But : Mettre à jour la position des éléments, vérifier les collisions et gérer la logique du jeu.
#       - Entrées : Aucune.
#       - Sorties :
#           - "You won!" si tous les aliens ont été détruits.
#           - "Game Over" si un alien atteint la position du vaisseau.
#
#   - check_collision_with_aliens :
#       - But : Vérifier les collisions entre les projectiles du vaisseau et les aliens.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - check_collision_with_player :
#       - But : Vérifier les collisions entre les projectiles des aliens et le vaisseau.
#       - Entrées : Aucune.
#       - Sorties :
#           - True si le vaisseau est touché et n'a plus de vie.
#           - False sinon.
#
#   - check_collision_with_protections :
#       - But : Vérifier les collisions entre les projectiles du vaisseau/aliens et les protections.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - reset_game :
#       - But : Réinitialiser l'état du jeu pour un nouveau départ.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - check_collision_with_aliens :
#       - But : Vérifier les collisions entre les projectiles du vaisseau et les aliens.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - check_collision_with_player :
#       - But : Vérifier les collisions entre les projectiles des aliens et le vaisseau.
#       - Entrées : Aucune.
#       - Sorties :
#           - True si le vaisseau est touché et n'a plus de vie.
#           - False sinon.
#
#   - check_collision_with_protections :
#       - But : Vérifier les collisions entre les projectiles du vaisseau/aliens et les protections.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - reset_game :
#       - But : Réinitialiser l'état du jeu pour un nouveau départ.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - draw_elements :
#       - But : Dessiner graphiquement les éléments du jeu sur le canevas.
#       - Entrées :
#           - canvas (Tkinter Canvas): L'objet Canvas sur lequel dessiner les éléments du jeu.
#       - Sorties : Aucune.
#
#   - update :
#       - But : Mettre à jour la position des éléments, vérifier les collisions et gérer la logique du jeu.
#       - Entrées : Aucune.
#       - Sorties :
#           - "You won!" si tous les aliens ont été détruits.
#           - "Game Over" si un alien atteint la position du vaisseau.
#--------------------------------------------------------------------------------------------------------------------

from Vaisseau import *
from Alien import *
from Protection import *

class Modele: 
    def __init__(self,fenetre):
        self.fenetre = fenetre
        self.vaisseau = Vaisseau()
        self.aliens = []
        self.create_aliens()
        self.should_reverse = False
        self.protections = []
        self.create_protections()
        self.score = 0


    def create_aliens(self):
        num_rows = 3
        num_columns = 7
        alien_width = 65
        alien_height = 60
        margin = 10
        for row in range(num_rows):
            for column in range(num_columns):
                x = column * (alien_width + margin) + 50
                y = row * (alien_height + margin) + 50
                alien = Alien(x, y)
                self.aliens.append(alien)

    def create_protections(self):
        protection_width = 130  
        protection_height = 50 
        spacing = 110 
        num_rows = 1 
        num_columns = 3 

        for row in range(num_rows):
            for column in range(num_columns):
                x = (column * (protection_width + spacing)) + 100 
                y = (row * (protection_height + spacing)) + 400 
                protection = Protection(x, y)
                self.protections.append(protection)


    
    def update_alien_projectiles(self):
        for alien in self.aliens:
            for projectile in alien.projectiles:
                projectile.update()
            alien.projectiles = [projectile for projectile in alien.projectiles if not projectile.is_offscreen()]


    def move_aliens_down(self):
        for alien in self.aliens:
            alien.y += 15 


    def update(self):
        for alien in self.aliens:
            alien.update()

        for projectile in self.vaisseau.projectiles:
            projectile.update()

        self.update_alien_projectiles()
        
        self.check_collision_with_aliens()
        
        self.check_collision_with_protections()

        if not self.aliens:
            self.fenetre.destroy()
            return "You won!"

        if any( alien.y > 540 for alien in self.aliens):
            self.fenetre.destroy()
            return "Game Over"
        
        for protection in self.protections:
            if any( alien.y > 400 and (protection.x < alien.x < protection.x + 130 or  protection.x < alien.x +30 < protection.x) for alien in self.aliens):
                self.protections.remove(protection)
                self.aliens.remove(alien)
        

        if any(alien.check_collision() for alien in self.aliens):
            self.move_aliens_down()
            self.should_reverse = not self.should_reverse


        if self.should_reverse:
            for alien in self.aliens:
                alien.direction *= -1


    def check_collision_with_aliens(self):
        for projectile in self.vaisseau.projectiles:
            for alien in self.aliens:
                if (
                    alien.x - 20 < projectile.x < alien.x + 16
                    and alien.y -10 < projectile.y < alien.y + 15
                ):
                    self.aliens.remove(alien)
                    self.vaisseau.projectiles.remove(projectile)
                    self.score += 25

    def check_collision_with_player(self):
        for alien in self.aliens:
            for projectile in alien.projectiles:
                if (
                    self.vaisseau.x - 30< projectile.x < self.vaisseau.x + 23
                    and self.vaisseau.y - 40 < projectile.y < self.vaisseau.y + 5
                ):

                    alien.projectiles.remove(projectile)
                    self.vaisseau.perte_vie()
                    if self.vaisseau.vie == 0:
                        self.fenetre.destroy()
                        return True
        return False
    

    def check_collision_with_protections(self):
        for projectile in self.vaisseau.projectiles:
            for protection in self.protections:
                if (
                    protection.x < projectile.x < protection.x + 130
                    and protection.y < projectile.y < protection.y + 50
                ):
                    self.vaisseau.projectiles.remove(projectile)
                    protection.perte_vie()
                    if protection.destruction():
                        self.protections.remove(protection)

        for alien in self.aliens:
            for projectile in alien.projectiles:
                for protection in self.protections:
                    if (
                        protection.x < projectile.x < protection.x + 130
                        and protection.y < projectile.y < protection.y + 50
                    ):
                        alien.projectiles.remove(projectile)
                        protection.perte_vie()
                        if protection.destruction():
                            self.protections.remove(protection)

    
    def reset_game(self):
        self.vaisseau = Vaisseau()
        self.vaisseau.projectiles = []  
        self.aliens = []
        self.create_aliens()
        self.protections = []
        self.create_protections()
        self.should_reverse = False





