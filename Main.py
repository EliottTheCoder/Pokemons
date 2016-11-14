# -*- coding:Utf-8 -*-
import pickle
from LastVersion import *
from combats import *
from os import system

# Créer les fichiers
fichierAttaques = open('attaques', 'a')
fichierPokemons = open('Pokemons', 'a')
fichierTypes = open('Types', 'a')
fichierAttaques.close()
fichierPokemons.close()
fichierTypes.close()

print ('\n\n\n')
print('***************** Pokemon *****************')
print ('\n\n\n')

continuer = ""
while(continuer != "0"):

	print('\nQue voulez-vous faire ? Entrez le numéro correspondant :')
	print('\t1 : Paramétrage du jeu (persos/attaques/types)')
	print('\t2 : Voir tous les Pokemons / les attaques')
	print('\t3 : Supprimer un Pokemon / attaque')
	print('\t4 : Faire un combat !')
	print("\t5 : Notice")

	rep = -1
	while rep < 1 or rep > 5:
		try:
			rep = input("> ")
			rep = int(rep)
			
			if(rep == 1):
				print('\nVoulez-vous créer une attaque ou un pokémon ? Entrez le numéro correspondant :')
				print('\t1 : Créer un pokemon')
				print('\t2 : Créer une attaque')
				print('\t3 : Créer un type\n')
				
				rep = -1
				while(rep < 1 or rep > 2):
					try: 
						rep = input('> ')
						rep = int(rep)
						print("\n")
						if rep == 1:
							CreationPokemon()
						elif rep == 2:
							CreationAttaque()
						elif rep == 3:
							CreationType()
						else:
							print("Saisie erronée.")
							print('Voulez-vous créer une attaque ou un pokemon ? Entrez le numéro correspondant :')
					except ValueError:
						print("Vous devez entrer un nombre.")
						rep = -1
		
			elif(rep == 2):
				if nbChoses("Pokemons") == 0 and nbChoses("attaques") == 0 and nbChoses("Types") == 0:
					print("Il n'y a ni pokemons, ni attaques, ni types.")
				else:
					print("Voulez-vous voir les Pokemons (1), les attaques (2) ou les types (3) ?")
					rep = -1
					while(rep < 1  or rep > 3):
						try:
							rep = input("> ")
							rep = int(rep)
							print("\n")
							if(rep == 1):
								voirChose("Pokemons")
							elif(rep == 2):
								voirChose("attaques")
							elif(rep == 3):
								voirChose("Types")
							else:
								print("Saisie erronée.")
								print("Que voulez vous faire ? Entrez le numéro correspondant : ")
						except ValueError:
							print("Vous devez entrer un nombre.")
							rep = -1
			elif(rep == 3):
				if nbChoses("Pokemons") == 0 and nbChoses("attaques") == 0 and nbChoses("Types") == 0:
					print("Il n'y a ni pokemons, ni attaques, ni types.")
				else:
					print ("Supprimer un perso (1), une attaque (2) ou un type (3) / TOUT SUPPRIMER (4) ? Entrez le num correspondant : ")
					rep = -1
					while rep < 1 or rep > 4:
						try:
							rep = input("> ")
							rep = int(rep)
							print("\n")
							if rep == 1:
								supprimerChose("Pokemons")
							elif rep == 2:
								supprimerChose("attaques")
							elif rep == 3:
								supprimerChose("Types")
							elif rep == 4:
								toutSupprimer()
							else:
								print("Saisie erronée.")
						except ValueError:
							print("Vous devez entrer un nombre.")
							rep = -1	
			elif(rep == 4):
				nbPokemon = nbChoses("Pokemons")
				if nbPokemon != 0:
					print("\n\nQuel pokemon choisissez vous ?")
					Moi = choisirPokemon()
					print("Quel est le pokemon de votre ennemi ?")
					Ennemi = choisirPokemon()
					combattre(Moi, Ennemi)
				else:
					print("Il n'y a pas de Pokemons.")
			elif rep == 5:
				print("Ce programme vous permet de créer vos Pokemons, avec lesquels vous pourrez faire des combats.")
				print("Tout d'abord, vous devez créer des types, puis des attaques et finalement vous pourrez créer vos pokemons.")
				print("ATTENTION, AUCUNE SECURITE N'EST APPORTEE POUR LE CHOIX DES ATTAQUES, ET LA SAISIE DES TYPES.")
				print("Si toutefois vous vous trompez, vous pouvez supprimer et recréer l'élément.")
			else:
				print("\nSaisie erronée.")
				print('Que voulez-vous faire ? Entrez le numéro correspondant :')
		except ValueError:
			print("Vous devez entrer un nombre !")
	
		print('\nVoulez-vous continuer (1) ou quitter (0) : ')
		continuer = input('> ')
		print("\n")

print('Bye !')

system("pause")
