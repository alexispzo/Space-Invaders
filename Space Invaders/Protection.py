#------------------------------------------------------------------------------------------------------------------
# Auteurs : BEN AMMAR Kenzi - BALLAND ALEXIS
# Date de réalisation : 17 Decembre 2023
# Objectifs de la classe Protection :
#   Cette classe représente une protection dans le contexte d'une application graphique utilisant Tkinter.
#   Elle est responsable de l'initialisation des propriétés de la protection, de la gestion de sa vie,
#   de la vérification de sa destruction, et du rendu graphique de la protection sur le canevas.
#
#   Méthodes principales :
#   - __init__ :
#       - But : Créer une instance de protection avec une position initiale et une vie spécifiées.
#       - Entrées :
#           - x (int): La position horizontale initiale de la protection.
#           - y (int): La position verticale initiale de la protection.
#       - Sorties : Aucune.
#
#   - draw :
#       - But : Afficher graphiquement la protection sous la forme d'un rectangle gris sur le canevas.
#       - Méthode : Utilise la méthode create_rectangle de Tkinter pour dessiner un rectangle représentant 
#                   la protection à sa position actuelle.
#       - Entrées :
#           - canvas (Tkinter Canvas): L'objet Canvas sur lequel dessiner la protection.
#       - Sorties : Aucune.
#
#   - perte_vie :
#       - But : Réduire la vie de la protection lorsqu'elle est touchée.
#       - Méthode : Décrémente la vie de la protection.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - destruction :
#       - But : Vérifier si la protection est détruite en fonction de sa vie restante.
#       - Méthode : Vérifie si la vie de la protection a atteint zéro.
#       - Sorties :
#           - detruite (bool): True si la protection est détruite, False sinon.
#       - Entrées : Aucune.
#--------------------------------------------------------------------------------------------------------------------


class Protection:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.vie = 3


    def perte_vie(self):
        self.vie -= 1
    

    def destruction(self):
        return self.vie == 0
    
    
    def draw(self, canvas):
        canvas.create_rectangle(self.x, self.y,self.x + 130, self.y + 50,fill='grey', outline='black')

    

        