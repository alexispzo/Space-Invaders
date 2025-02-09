#------------------------------------------------------------------------------------------------------------------
# Auteurs : BEN AMMAR Kenzi - BALLAND ALEXIS
# Date de réalisation : 17 Decembre 2023
# Objectifs de la classe Vue :
#   Cette classe représente la vue de l'application Space Invaders dans le contexte d'une interface graphique
#   utilisant Tkinter. Elle est responsable de la création des widgets, de l'affichage graphique des éléments
#   du jeu tels que le vaisseau, les aliens, les protections, ainsi que des informations comme le score et le
#   nombre de vies du joueur.
#
#   Méthodes principales :
#   - __init__ :
#       - But : Initialiser une instance de la classe Vue avec la fenêtre principale et le modèle associé.
#       - Méthode : Appelle le constructeur de la classe parente (Frame) avec la fenêtre principale et le modèle,
#         puis initialise les dimensions de la fenêtre, le titre, et crée les widgets avec la méthode create_widgets.
#       - Entrées :
#           - fenetre (Tkinter Toplevel): La fenêtre principale de l'application.
#           - modele (Modele): L'instance du modèle associé à la vue.
#       - Sorties : Aucune.
#
#   - create_widgets :
#       - But : Créer les widgets nécessaires à l'interface utilisateur.
#       - Méthode : Crée un cadre (frame) pour les boutons, labels, et le canevas. Initialise des boutons pour
#         commencer un nouveau jeu et quitter, des labels pour afficher le nombre de vies et le score, ainsi qu'un
#         canevas pour afficher graphiquement les éléments du jeu.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - draw :
#       - But : Rafraîchir l'affichage graphique de la vue avec les éléments actuels du jeu.
#       - Méthode : Efface le contenu du canevas, puis appelle les méthodes draw des objets du modèle (vaisseau,
#         aliens, protections) pour les redessiner. Met également à jour les labels affichant le score et le nombre
#         de vies du joueur.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#
#   - start_new_game :
#       - But : Initialiser un nouveau jeu en réinitialisant le modèle.
#       - Méthode : Appelle la méthode reset_game du modèle pour réinitialiser toutes les données du jeu, puis
#         appelle la méthode draw pour mettre à jour l'affichage.
#       - Entrées : Aucune.
#       - Sorties : Aucune.
#--------------------------------------------------------------------------------------------------------------------



from tkinter import Button, Frame, Label, PhotoImage, Canvas, Tk, CENTER
 
class Vue(Frame):
    def __init__(self, fenetre, modele): 
        super().__init__(fenetre)
        self.modele = modele
        self.largeur = fenetre.winfo_screenwidth() - 100
        self.hauteur = fenetre.winfo_screenheight() - 50
        fenetre.title("SpaceInvaders")

        self.create_widgets()


    def create_widgets(self): 
     
        frame = Frame(self)
        frame.pack(side='right', padx=20)
     
        self.lives = Label(frame)
        self.lives.pack()

        self.score = Label(frame, text='Score : ')
        self.score.pack()

        new = Button(frame, text='New Game', command=self.start_new_game)
        new.pack()

        quit = Button(frame, text='Quit', command=self.quit)
        quit.pack()

    
        self.canvas = Canvas(self, width=800, height=600, bg='black')
        self.canvas.pack()
        
        self.canvas.focus_set()


    def draw(self):
        self.canvas.delete("all")
        
        self.modele.vaisseau.draw(self.canvas)
        
        for alien in self.modele.aliens:
            alien.draw(self.canvas)
        
        for projectile in self.modele.vaisseau.projectiles:
            projectile.draw(self.canvas)
        
        for protection in self.modele.protections:
            protection.draw(self.canvas)

        self.lives.config(text= 'Lives : ' + str(self.modele.vaisseau.vie)) #displaying player lives
        
        self.score.config(text='Score : ' + str(self.modele.score)) #displaying score


    def start_new_game(self):
        self.modele.reset_game()
        
        self.draw()








