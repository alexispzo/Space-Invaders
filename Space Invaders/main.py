#--------------------------------------------------------------------------------------------------------------------
# Auteurs : BEN AMMAR Kenzi - BALLAND ALEXIS
# Date de réalisation : 17 Decembre 2023
# Objectifs du fichier : 
#     Ce fichier fait partie d'une application graphique utilisant Tkinter.
#     Il initie les éléments nécessaires tels que le modèle, la vue, et le contrôleur, 
#     puis lance la boucle principale de l'application.
#     Les objectifs spécifiques de ce fichier incluent l'initialisation des composants 
#     principaux de l'applicationet le démarrage de son exécution.   
#---------------------------------------------------------------------------------------------------------------------


from tkinter import Tk
from vue import Vue 
from Vaisseau import Vaisseau
from Controleur import Controleur
from Modele import Modele

fenetre = Tk()          
modele = Modele(fenetre)
view = Vue(fenetre,modele)
view.pack()
controleur = Controleur(fenetre,view,modele)
controleur.run()             








