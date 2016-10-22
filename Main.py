# -*- coding:Utf-8 -*-
import pickle
from LastVersion import *
from os import system

print ('\n\n\n')
print('***************** Pokemon *****************')
print ('\n\n\n')

continuer = 1

while(continuer != 0):

	print('Que voulez-vous faire ? Entrez le numéro correspondant :')
	print('\t1 : Paramétrage du jeu (persos et attaques)')
	print('\t2 : Voir tous les Pokemons')

	rep = input('> ')

	if(rep == '1'):
	
		print('\nVoulez-vous créer une attaque ou un pokémon ? Entrez le numéro correspondant :')
		print('\t1 : Créer un pokemon')
		print('\t2 : Créer une attaque\n')
	
		rep = input('> ')
		print('\n')
		
		if(rep == '1'):
			CreationPokemon()
		else:
			CreationAttaque()
	else:
		voirPokemons()
	
	print('\nVoulez vous continuer (1) ou quitter (0) : ')
	continuer = input('> ')
	continuer = int(continuer)

print('Bye !')

system("pause")