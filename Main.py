# -*- coding:Utf-8 -*-
import pickle
from LastVersion import *
from os import system

print ('\n\n\n')
print('***************** Pokemon *****************')
print ('\n\n\n')

continuer = ""
while(continuer != "0"):

	print('Que voulez-vous faire ? Entrez le numéro correspondant :')
	print('\t1 : Paramétrage du jeu (persos et attaques)')
	print('\t2 : Voir tous les Pokemons')

	rep = ""
	while rep != "1" and rep != "2":
		
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
					print("Le pokémon a été enregistré")
					rep = "1"
				elif(rep =="2"):
					print("\n")
					CreationAttaque()
					print("L'attaque a été enregistrée !")
				else:
					print("\nSaisie erronée.")
					print('Voulez-vous créer une attaque ou un pokemon ? Entrez le numéro correspondant :')
		
		elif(rep == "2"):
			voirPokemons()
		else:
			print("\nSaisie erronée.")
			print('Que voulez-vous faire ? Entrez le numéro correspondant :')

	print('\nVoulez-vous continuer (1) ou quitter (0) : ')
	continuer = input('> ')
	print("\n")

print('Bye !')

system("pause")
