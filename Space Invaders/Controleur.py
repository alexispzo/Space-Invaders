#------------------------------------------------------------------------------------------------------------------
# Auteurs : BEN AMMAR Kenzi - BALLAND ALEXIS
# Date de réalisation : 17 Decembre 2023
# Objectifs de la classe Controleur :
#   Cette classe agit en tant que contrôleur principal dans une application graphique utilisant Tkinter.
#   Elle est responsable de la gestion des entrées utilisateur, de la liaison des touches aux actions du vaisseau,
#   de l'exécution continue du jeu, de la mise à jour des éléments graphiques, et de la détection des collisions.
#
#   Méthodes principales :
#   - __init__ :
#       - But : Créer une instance de Controleur avec les éléments principaux.
#       - Entrées :
#           - fenetre (Tkinter Tk): L'objet principal de la fenêtre Tkinter.
#           - vue (Vue): L'objet Vue responsable du rendu graphique.
#           - modele (Modele): L'objet Modele contenant la logique du jeu.
#       - Sorties : Aucune.
#
#   - left_key :
#       - But : Gérer l'événement de pression de la touche gauche pour déplacer le vaisseau vers la gauche.
#       - Méthode : Appelle la méthode deplacement_gauche du vaisseau dans le modèle.
#       - Entrées :
#           - event (Tkinter Event): L'événement lié à la pression de la touche gauche.
#       - Sorties : Aucune.
#
#   - right_key :
#       - But : Gérer l'événement de pression de la touche droite pour déplacer le vaisseau vers la droite.
#       - Méthode : Appelle la méthode deplacement_droite du vaisseau dans le modèle.
#       - Entrées :
#           - event (Tkinter Event): L'événement lié à la pression de la touche droite.
#       - Sorties : Aucune.
#
#   - space_key :
#       - But : Gérer l'événement de pression de la touche espace pour déclencher le tir du vaisseau.
#       - Méthode : Appelle la méthode tirer du vaisseau dans le modèle.
#       - Entrées :
#           - event (Tkinter Event): L'événement lié à la pression de la touche espace.
#       - Sorties : Aucune.
#
#   - run :
#       - But : Exécuter la boucle principale du jeu avec la liaison des touches et la mise à jour continue.
#               Cela permet de maintenir l'interaction utilisateur et d'actualiser les éléments du jeu en temps réel.
#       - Méthode : Lie les touches gauche, droite et espace aux méthodes correspondantes. Puis, exécute une boucle
#                   continue qui met à jour la vue, le modèle, et vérifie les collisions.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - update :
#       - But : Mettre à jour les éléments graphiques, exécuter la logique du jeu, et vérifier les collisions.
#               Cette méthode est appelée de manière répétitive pour maintenir le fonctionnement continu du jeu.
#       - Méthode : Appelle la méthode draw de la vue pour mettre à jour l'affichage, puis appelle la méthode
#         update du modèle pour exécuter la logique du jeu. Enfin, vérifie les collisions avec la méthode
#         check_collision_with_player du modèle.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#--------------------------------------------------------------------------------------------------------------------


from Vaisseau import Vaisseau
from Modele import Modele


class Controleur:
    def __init__(self, fenetre, vue, modele):
        self.fenetre = fenetre
        self.vue = vue
        self.modele = modele


    def left_key(self, event):
        self.modele.vaisseau.deplacement_gauche()


    def right_key(self, event):
        self.modele.vaisseau.deplacement_droite()


    def space_key(self, event):
        self.modele.vaisseau.tirer()    


    def run(self): 
        self.fenetre.bind("<Left>", self.left_key)
        self.fenetre.bind("<Right>", self.right_key)
        self.fenetre.bind("<space>", self.space_key)  
        self.fenetre.after(10, self.update)
        self.fenetre.mainloop()

    def update(self):
        self.vue.draw()
        self.modele.update()
        if self.modele.check_collision_with_player():
            return "Game Over"
        else:
            self.fenetre.after(10, self.update)