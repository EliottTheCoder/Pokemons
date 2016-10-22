# -*- coding:Utf-8 -*-
import pickle

class Personnage:
	"""Classe définissant un personnage, avec une vitesse, une force, une barre de vie"""
	
	def __init__(self, nom, pt_vie, vitesse, force, attaques):
		"""Attribut le nom, pt de vie, vitesse, force"""
		self.nom = nom
		self.pt_vie = pt_vie
		self.vitesse = vitesse
		self.force = force
		self.attaques = attaques

	def caracteristiques(self):
		"""Donne les caracteristiques du pokemon"""
		print("Pokemon : {}".format(self.nom))
		print("Point de vie : {}".format(self.pt_vie))
		print("Vitesse : {}".format(self.vitesse))
		print("Force : {}".format(self.force))
		
class Attaque:
		""" Classe définissant les attaques utilisées par les pokémons """
	
		def __init__(self, nom, degats):
			self.nom = nom
			self.degats = degats
			
		def caracteristiques(self):
			"""Donne les caracteristiques de l'attaque """
			print("Attaque : {}".format(self.nom))
			print("Dégâts : {}".format(self.degats))
			print("\n")

def PrendreContenuFichier(fichierARecuperer, mode):
	""" Récupère le contenu d'un fichier pour le remettre avant d'écrire dessus """
	with open(fichierARecuperer, mode) as fichier:
		contenu = fichier.read()
		fichier.close()
	return contenu
			
def CreationAttaque():
	""" Créé une attaque selon les entrées de l'admin """
	print('Créez vos attaques !')
	print('Choisissez un nom : ')
	nom = input('> ') 
	print('\nChoisissez les dégâts de cette attaque : ')
	degats = input('> ')
		
	AttaqueCree = Attaque(nom, degats)
	enregistrerAttaque(AttaqueCree)

def enregistrerAttaque(Attaque):
	""" Enregistre une attaque """
	contenu = PrendreContenuFichier("Attaques", "rb")
	
	with open('Attaques', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		fichier.write(contenu)
		mon_pickler.dump(Attaque)

def CreationPokemon():	
	""" Créé un pokemon selon les entrées de l'admin """
	print('Vous avez toujours rêvé de créer vos propres pokémons ? Vous pouvez enfin le faire !')
	print('Choisissez un nom : ')
	nom = input('> ') 
	print('\nChoisissez le nb de pt de vie du pokemon : ')
	pt_vie = input('> ')
	print('\nChoisissez la vitesse du pokemon : ')
	vitesse = input('> ')
	print('\nChoisissez la force du pokemon : ')
	force = input('> ')
	print('\n')
	
	attaques = ChoisirAttaque() # Renvoie une liste de 4 objets Attaques
	
	PokemonCree = Personnage(nom, pt_vie, vitesse, force, attaques)
	enregistrerPerso(PokemonCree)
	
def enregistrerPerso(Personnage):
	""" Enregistre un pokemon """
	contenu = PrendreContenuFichier("Pokemons", "rb")
	
	with open('Pokemons', 'wb') as fichier:
		mon_pickler = pickle.Pickler(fichier)
		fichier.write(contenu)
		mon_pickler.dump(Personnage)

def ChoisirAttaque():
	
	AttaquePrise = Attaque("Attaque", "10")
	dicoAttaques = {}

	fichier = open('attaques', 'rb')
	mon_depickler = pickle.Unpickler(fichier)
	i = 0

	try:
		while True:
			AttaquePrise = mon_depickler.load()
			dicoAttaques[i] = AttaquePrise
			#AttaquePrise.caracteristiques()
			i+=1
	except EOFError:
		pass

	fichier.close()		
	
	i = 0
	print('Voici les attaques dispos : ')
	while i < len(dicoAttaques):
		print('Attaque', i,' : ', dicoAttaques[i].nom, ' = ', dicoAttaques[i].degats)
		i += 1

	print("Vous pouvez choisir 4 attaques parmis les dernières... Lesquelles choisissez-vous ? Entrez les numéros correspondants")
	
	i = 0
	attaquesChoisies = {}
	while i < 4:
		print("Attaque", i + 1 , " : ")
		attaquesChoisies[i] = input("> ") 
		attaquesChoisies[i] = int(attaquesChoisies[i])
		i += 1
	
	print('Vous avez choisi les attaques : ')
	print(dicoAttaques[attaquesChoisies[0]].nom, ", ", dicoAttaques[attaquesChoisies[1]].nom, ", ", dicoAttaques[attaquesChoisies[2]].nom, " et ", dicoAttaques[attaquesChoisies[3]].nom)

	attaques = [dicoAttaques[attaquesChoisies[0]], dicoAttaques[attaquesChoisies[1]], dicoAttaques[attaquesChoisies[2]], dicoAttaques[attaquesChoisies[3]]]

	return attaques

def voirPokemons():
	
	print("\n")
	with open('Pokemons', 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		try:
			while True:
				Pokemon = mon_depickler.load()
				Pokemon.caracteristiques()
				print("\n")
				i = 0
				while i < 4:
					Pokemon.attaques[i].caracteristiques()
					i += 1
		except EOFError:
			pass
		