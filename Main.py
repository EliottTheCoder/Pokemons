# -*- coding:Utf-8 -*-
import pickle
from LastVersion import *
from os import system

print ('\n\n\n')
print('***************** Pokemon *****************')
print ('\n\n\n')

CreerFichiers()

continuer = ""
while(continuer != "0"):

	print('\nQue voulez-vous faire ? Entrez le numéro correspondant :')
	print('\t1 : Paramétrage du jeu (persos et attaques)')
	print('\t2 : Voir tous les Pokemons / les attaques')
	print('\t3 : Supprimer un Pokemon / attaque')

	rep = ""
	while rep != "1" and rep != "2" and rep != "3":
		rep = input("> ")
		if(rep == "1"):
			
			print('\nVoulez-vous créer une attaque ou un pokémon ? Entrez le numéro correspondant :')
			print('\t1 : Créer un pokemon')
			print('\t2 : Créer une attaque\n')
			
			rep = ""
			while(rep != "1" and rep != "2"):
				rep = input('> ')
				if(rep == "1"):
					print("\n")
					CreationPokemon()
					
					rep = "1"
				elif(rep =="2"):
					print("\n")
					CreationAttaque()
					print("L'attaque a été enregistrée !")
				else:
					print("\nSaisie erronée.")
					print('Voulez-vous créer une attaque ou un pokemon ? Entrez le numéro correspondant :')
		
		elif(rep == "2"):
			print("Voulez-vous voir les Pokemons (1) ou les attaques (2) ?")
			rep = ""
			while(rep != "1" and rep != "2"):
				rep = input("> ")
				print("\n")
				if(rep == "1"):
					voirChose("Pokemons")
				elif(rep == "2"):
					voirChose("attaques")
				else:
					print("Saisie erronée.")
					print("Que voulez vous faire ? Entrez le numéro correspondant : ")
		
		elif(rep == "3"):
			print ("Supprimer un perso (1) ou une attaque (2) ? Entrez le num correspondant : ")
			rep = ""
			while rep != "1" and rep != "2":
				rep = input("> ")
				print("\n")
				if rep == "1":
					supprimerChose("Pokemons")
				elif rep == "2":
					supprimerChose("attaques")
		else:
			print("\nSaisie erronée.")
			print('Que voulez-vous faire ? Entrez le numéro correspondant :')

	print('\nVoulez-vous continuer (1) ou quitter (0) : ')
	continuer = input('> ')
	print("\n")

print('Bye !')

system("pause")
