# -*- coding:utf-8 -*-

from random import *
from os import system
import pickle
from LastVersion import * 

def choisirAttaqueCombat(Pokemon, humainOuOrdi):
	
	dicoAttaques = {}
	i = 0
	if humainOuOrdi == True:
		print('Voici vos attaques : \n')
	
	while i < 4:
		if humainOuOrdi == True:
			print(i + 1)
			print (Pokemon.attaques[i].caracteristiques())
			print('\n')
		dicoAttaques[i] = Pokemon.attaques[i]
		i += 1
	
	if humainOuOrdi == True:
		attaque = creerVar("Quelle attaque voulez-vous utiliser ? Entrez le num : ", 1, 4) - 1
	else:
		attaque = randint(0, 3)
	
	AttaqueChoisie = dicoAttaques[attaque]
	return AttaqueChoisie
	
def attaquer(Attaquant, Defenseur, humainOuOrdi):

	Attaque = choisirAttaqueCombat(Attaquant, humainOuOrdi)
	print("\n" + Attaquant.nom + " envoie l'attaque " + Attaque.nom + " sur " + Defenseur.nom + " !!")
	
	degatsAttaque = (Attaque.degats + Attaquant.force) / 10 * randint(1, 2)
	
	if Attaque.type.avantage == Defenseur.type.nom:
		degatsAttaque *= 1.5
		print("L'attaque est efficace !")
	elif Attaque.type.desavantage == Defenseur.type.nom:
		degatsAttaque *= 0.75
		print("L'attaque n'est pas efficace...")
	else:
		print("L'attaque est normale.")
	Defenseur.pt_vie -= degatsAttaque
	
	
	print("L'attaque inflige ", degatsAttaque, " dégâts.")
	if humainOuOrdi == False:
		if Defenseur.pt_vie < 0:
			print("Vous avez 0pv.\n")
		else:
			print("Vous n'avez plus que ", Defenseur.pt_vie, " pv\n")
	else:
		if Defenseur.pt_vie < 0:
			print(Defenseur.nom, " ennemi a 0pv.\n")
		else:
			print(Defenseur.nom, " ennemi n'a plus que ", Defenseur.pt_vie, " pv\n")
	
	return Defenseur.pt_vie
	
def combattre(Utilisateur, Ennemi): 
	
	print("********** COMBAT : ", Utilisateur.nom, " VS ", Ennemi.nom, " **********\n\n\n")
	
	print("Vous avez ", Utilisateur.pt_vie, " pv.")
	print(Ennemi.nom, " a ", Ennemi.pt_vie, " pv.\n\n")
	
	while(Utilisateur.pt_vie > 0 and Ennemi.pt_vie > 0):
		
		if(Utilisateur.vitesse > Ennemi.vitesse):
			print("Vous êtes plus rapide et vous attaquez en premier !\n")
			Ennemi.pt_vie = attaquer(Utilisateur, Ennemi, True) # True humain, False ordi
			if(Ennemi.pt_vie > 0):
				Utilisateur.pt_vie = attaquer(Ennemi, Utilisateur, False)
				# Utilisateur commence
		else:
			print(Ennemi.nom, " ennemi est plus rapide et attaque en premier !\n")
			Utilisateur.pt_vie = attaquer(Ennemi, Utilisateur, False)
			if(Utilisateur.pt_vie > 0):
				Ennemi.pt_vie = attaquer(Utilisateur, Ennemi, True)
				# Ordi commence
	
	print("Combat fini !")
	
	if Utilisateur.pt_vie < 0:
		print("Vous avez perdu. Rejouez une prochaine fois !")
	else:
		print("Vous avez gagné ! Félicitation !")
	