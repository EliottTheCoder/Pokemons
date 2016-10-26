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
			#print("\n")

def CreationAttaque():
	""" Créé une attaque selon les entrées de l'admin """
	DEGATS_MAX = 200
	print('Créez vos attaques !\n')
	
	rep = False
	while rep == False:	
		print('Choisissez un nom : ')
		nom = input('> ') 
		rep = verifierChose("attaques", nom) # Retourne False si l'attaque existe
		if rep == False:
			print("Cette attaque existe déjà.\n")

	degats = -100
	while degats <= 0 or degats > DEGATS_MAX:
		try:
			print('\nChoisissez les dégâts de cette attaque : ')
			degats = input('> ')
			degats = int(degats)
			if degats <= 0:
				print("Les dégâts de l'attaque doivent être positifs.")
			if degats > DEGATS_MAX:
				print("Les dégâts de l'attaque doivent être inférieurs à DEGATS_MAX, donc : ", DEGATS_MAX)
		except ValueError:
			print("Vous devez entrez un nombre.")
			degats = -100
	
	AttaqueCree = Attaque(nom, degats)
	enregistrerChose("attaques", AttaqueCree)

def CreationPokemon():	
	""" Créé un pokemon selon les entrées de l'admin """
	
	PV_MAX = 300
	VITESSE_MAX = 100
	FORCE_MAX = 100
	nb_attaques = nbChoses("attaques")
	
	if nb_attaques < 4:
		print("Il n'y a pas assez d'attaques pour créer un pokémon.")
	else:
		print('Vous avez toujours rêvé de créer vos propres pokémons ? Vous pouvez enfin le faire !\n')

		rep = False
		while rep == False:	
			print('Choisissez un nom : ')
			nom = input('> ') 
			rep = verifierChose("Pokemons", nom)
			if rep == False:
				print("Ce pokemon existe déjà.\n")
	
		pt_vie = -100
		while pt_vie <= 0 or pt_vie > PV_MAX:
			try:
				print('\nChoisissez le nombre de points de vie du pokemon : ')
				pt_vie = input('> ')
				pt_vie = int(pt_vie)
				if pt_vie <= 0:
					print("Le nombre de points de vie doit être supérieur à 0")
				if pt_vie > PV_MAX:
					print("Le nombre de points de vie doit être inférieur au PV_MAX, donc : ", PV_MAX)
			except ValueError:
				print("Vous devez entrer un nombre.")
				pt_vie = -100
	
		vitesse = -100
		while vitesse <= 0 or vitesse > VITESSE_MAX:
			try:
				print('\nChoisissez la vitesse du pokemon : ')
				vitesse = input('> ')
				vitesse = int(vitesse)
				if vitesse <= 0:
					print("Le nombre de points de vitesse doit être positif.")
				if vitesse > VITESSE_MAX:
					print("Le nombre de points de vitesse doit être inférieur a VITESSE_MAX, donc : ", VITESSE_MAX)
			except ValueError:
				print("Vous devez entrer un nombre")
				vitesse = -100
	
		force = -100
		while force <= 0 or force > FORCE_MAX:
			try:
				print('\nChoisissez la force du pokemon : ')
				force = input('> ')
				force = int(force)
				if force <= 0:
					print("Le nombre de points de force doit être positif.")
				if force > FORCE_MAX:
					print("Le nombre de points de force doit être inférieur a FORCE_MAX, donc : ", FORCE_MAX)
			except ValueError:
				print("Vous devez entrer un nombre")	
				force = -100
	
		attaques = ChoisirAttaque() # Renvoie une liste de 4 objets Attaques
	
		PokemonCree = Personnage(nom, pt_vie, vitesse, force, attaques)
		enregistrerChose("Pokemons", PokemonCree)

def enregistrerChose(type, objet):
	""" Enregistre un perso ou une attaque """
	contenu = PrendreContenuFichier(type, "rb")
	
	with open(type, "wb") as fichier:
		mon_pickler = pickle.Pickler(fichier)
		fichier.write(contenu)
		mon_pickler.dump(objet)
		
def ChoisirAttaque():
	""" Attribut des attaques à un perso """
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
		try:
			attaquesChoisies[i] = int(attaquesChoisies[i])
			if attaquesChoisies[i] < len(dicoAttaques) and attaquesChoisies[i] >= 0:
				i += 1
			else:
				print("Ce numéro ne correspond à aucune attaque.")
		except ValueError:
			print("Vous devez entrer un nombre.")
	
	print('Vous avez choisi les attaques : ')
	print(dicoAttaques[attaquesChoisies[0]].nom, ", ", dicoAttaques[attaquesChoisies[1]].nom, ", ", dicoAttaques[attaquesChoisies[2]].nom, " et ", dicoAttaques[attaquesChoisies[3]].nom)

	attaques = [dicoAttaques[attaquesChoisies[0]], dicoAttaques[attaquesChoisies[1]], dicoAttaques[attaquesChoisies[2]], dicoAttaques[attaquesChoisies[3]]]

	return attaques

def verifierChose(type, nomChose):
	""" Verifie l'existence d'un objet """
	with open(type, 'rb')as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		try:
			while True:
				Chose = mon_depickler.load()
				if Chose.nom == nomChose:
					return False
		except EOFError:
			return True
				
def CreerFichiers():
	""" Initialisation, créé les fichiers attaques et Pokemons s'il n'existent pas """
	contenu = PrendreContenuFichier('fichier.txt', 'r')
	if contenu == "0":
		fichiersAttaques = open('attaques', 'wb')
		fichiersPokemons = open('Pokemons', 'wb')
		fichiersAttaques.close()
		fichiersPokemons.close()
		fichier = open('fichier.txt', 'w')
		fichier.write("1")
		fichier.close()

def voirChose(type):
	""" Affiche une liste des objets """
	with open(type, 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		nb = 0
		try:
			while True:
				Chose = mon_depickler.load()
				print("\n")
				Chose.caracteristiques()
				print("\n")
				if type == "Pokemons":
					i = 0
					while i < 4:
						Chose.attaques[i].caracteristiques()
						i += 1
				nb += 1
		except EOFError:
			if nb == 0:
				print("Il n'y a pas encore de ", type)
				
def supprimerChose(type):
	""" Supprime un objet """
	if nbChoses(type) == 0:
		print("Il n'y a pas de ", type)
	
	else:
		if type == "Pokemons":
			question = "Quel pokémon voulez-vous supprimer ?"
			reponse = "Ce pokémon n'existe pas."
		else:
			question = "Quelle attaques voulez-vous supprimer ?"
			reponse = "Cette attaque n'existe pas."
	
		rep = True
		while rep == True:
			print(question, " Tapez 1 pour voir la liste")
			nom = input('> ')
			if nom == "1":
				if type == "Pokemons":
					voirChose("Pokemons")
				else:
					voirChose("attaques")
			else:
				rep = verifierChose(type, nom)
				if rep == True:
					print(reponse)
	
		with open(type, 'rb') as fichier:
			mon_depickler = pickle.Unpickler(fichier)
			i = 0
			ok = True
			Choses = {}
			while ok == True:
				try:
					Chose = mon_depickler.load()
					if Chose.nom != nom:
						Choses[i] = Chose
						i += 1
				except EOFError:
					ok = False
	
		with open(type, 'wb') as fichier:
			mon_pickler = pickle.Pickler(fichier)
			i = 0
			while i < len(Choses):
				mon_pickler.dump(Choses[i])
				i += 1
		print("Le/la ", type, " a bien été supprimé(e)")
		
def nbChoses(type):
	""" Renvoie le nb d'objets """
	with open(type, "rb") as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		i = 0
		try:
			while True:
				Objet = mon_depickler.load()
				i += 1
		except EOFError:
			return i
				
def PrendreContenuFichier(fichierARecuperer, mode):
	""" Récupère le contenu d'un fichier pour le remettre avant d'écrire dessus """
	with open(fichierARecuperer, mode) as fichier:
		contenu = fichier.read()
		fichier.close()
	return contenu
