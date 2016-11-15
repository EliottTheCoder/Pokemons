# -*- coding:Utf-8 -*-
import pickle

DEGATS_MAX = 200
PV_MAX = 300
VITESSE_MAX = 100	
FORCE_MAX = 100
PORTEE_MAX = 10

def definirVarMax():
	
	DEGATS_MAX = creerVar("Quels sont les degats max d'une attaque ? ", 1, 100000)
	PV_MAX = creerVar("Quels sont les pv max d'un pokemon ? ", 1, 100000)
	VITESSE_MAX = creerVar("Quelle est la vitesse max d'un pokemon ? ", 1, 100000)
	FORCE_MAX = creerVar("Quelle est la force max d'un pokemon ? ", 1, 100000)
	PORTEE_MAX = creerVar("Quelle est la portée max d'une attaque ? ", 1, 100000)
	
	with open('parametres.txt', 'w') as fichier:
		fichier.write(str(DEGATS_MAX) + '\n' + str(PV_MAX) + '\n' + str(VITESSE_MAX) + '\n' + str(FORCE_MAX) + '\n' + str(PORTEE_MAX))

class Personnage:
	"""Classe définissant un personnage, avec une vitesse, une force, une barre de vie"""
	
	def __init__(self, nom, pt_vie, vitesse, force, type, attaques):
		"""Attribut le nom, pt de vie, vitesse, force"""
		self.nom = nom
		self.pt_vie = pt_vie
		self.vitesse = vitesse
		self.force = force
		self.type = type
		self.attaques = attaques

	def caracteristiques(self):
		"""Donne les caracteristiques du pokemon"""
		print("Pokemon : ", self.nom)
		print("Point de vie : ", self.pt_vie)
		print("Vitesse : ", self.vitesse)
		print("Force : ", self.force)
		print("Type : ", self.type.nom)
		
class Attaque:
		""" Classe définissant les attaques utilisées par les pokémons """
	
		def __init__(self, nom, type, degats, portee):
			self.nom = nom
			self.degats = degats
			self.type = type
			self.portee = portee
			
		def caracteristiques(self):
			"""Donne les caracteristiques de l'attaque """
			print("Attaque : ", self.nom)
			print("Dégâts : ", self.degats)
			print("Portée : ", self.portee)
			print("Type : ", self.type.nom)

class Type:
	""" Classe définissant le type d'une attaque ou d'un pokemon """
	
	def __init__(self, nom, avantage, desavantage):
		self.avantage = avantage
		self.desavantage = desavantage
		self.nom = nom
			
	def caracteristiques(self):
		print("Type : ", self.nom)
		print("Avantage sur : ", self.avantage)
		print("Désavantage sur : ", self.desavantage)
		
def CreationType():
	""" Créé un type """
	
	print("Créez des nouveaux types !\n")
	
	rep = False
	while rep == False:	
		print('Choisissez un nom : ')
		nom = input('> ') 
		rep = verifierChose("Types", nom) # Retourne False si l'attaque existe
		if rep == False or nom == "":
			print("Ce type existe déjà.\n")
			nom = False
			
	avantage = nom
	while avantage == nom:
		print("Quel est le type face auquel il a un avantage ?")
		avantage = input("> ")
		if avantage == nom:
			print("Un type ne peut pas être aventagé par lui-même.")
		else:
			print("Le type ", nom, " est avantagé face au type ", avantage)
	
	desavantage = nom
	while desavantage == nom:
		print("Quel est le type face auquel il est désaventagé ?")
		desavantage = input("> ")
		if desavantage == nom:
			print("Un type ne peut pas être désaventagé par lui-même.")
		else:
			print("Le type ", nom, " est désaventagé face au type ", desavantage)	
	
	TypeCree = Type(nom, avantage, desavantage)
	enregistrerChose("Types", TypeCree)
	print("Le type a été enregistré !")

def creerVar(phrase, min, max):
	
	var = -1
	while var <= 0 or var > max:
		try:
			if phrase != "":
				print('\n' + phrase)
			var = int(input('> '))
			if var <= 0:
				print("Le nb doit être positif.")
			if var > max:
				print("Le nombre doit être inférieur ou égal au max, ici : ", max)
		except ValueError:
			print("Vous devez entrez un nombre.")
			var = -1
	
	return var
	
def CreationAttaque():
	""" Créé une attaque selon les entrées de l'admin """

	if nbChoses("Types") < 1:
		print("Il n'y a pas de type, vous devez d'abord créer une attaque.")
	else:
		print('Créez vos attaques !\n')
	
		rep = False
		while rep == False:	
			print('Choisissez un nom : ')
			nom = input('> ') 
			rep = verifierChose("attaques", nom) # Retourne False si l'attaque existe
			if rep == False or nom == "":
				print("Cette attaque existe déjà.\n")
				rep = False
	
	
		degats = creerVar("Choisissez les dégâts de cette attaque : ", 1, DEGATS_MAX)
		portee = creerVar("Choisissez la portée de cette attaque : ", 1, PORTEE_MAX)
	
		type = choisirChose("Types", 0)
		AttaqueCree = Attaque(nom, type, degats, portee)
		enregistrerChose("attaques", AttaqueCree)
		print("L'attaque a été enregistrée !")

def CreationPokemon():	
	""" Créé un pokemon selon les entrées de l'admin """
	
	if nbChoses("attaques") < 4:
		print("Il n'y a pas assez d'attaques pour créer un pokémon.")
	elif nbChoses("Types") < 1:
		print("Il n'y a pas de type, vous ne pouvez pas créer de Pokemon.")
	else:
		print('Vous avez toujours rêvé de créer vos propres pokémons ? Vous pouvez enfin le faire !\n')

		rep = False
		while rep == False:	
			print('Choisissez un nom : ')
			nom = input('> ') 
			rep = verifierChose("Pokemons", nom)
			if rep == False:
				print("Ce pokemon existe déjà.\n")
	
		pt_vie = creerVar("Choisissez le nombre de points de vie du pokemon : ", 1, PV_MAX)
		vitesse = creerVar("Choisissez la vitesse du pokemon : ", 1, VITESSE_MAX)
		force = creerVar("Choisissez la force du pokemon : ", 1, FORCE_MAX)
		
		type = choisirChose("Types", 0)
		print("\n")
		attaques = choisirChose("attaques", type) # Renvoie une liste de 4 objets Attaques
	
		PokemonCree = Personnage(nom, pt_vie, vitesse, force, type, attaques)
		enregistrerChose("Pokemons", PokemonCree)

def enregistrerChose(type, objet):
	""" Enregistre un perso ou une attaque """
	
	with open(type, "ab") as fichier:
		mon_pickler = pickle.Pickler(fichier)
		mon_pickler.dump(objet)

def choisirChose(type, typeAttaque):
	
	if type == "Types":
		Objet = (Type)
		phrase = "Quel type choisissez-vous ?"
		phrase2 = "Vous avez choisi ce type : "
	elif type == "Pokemons":
		Objet = (Personnage)
		phrase = "Quel Pokemon choisissez-vous ?"
		phrase2 = "Vous avez choisi ce Pokemon : "
	else:
		Objet = (Attaque)
		phrase = "Quelle attaque choisissez-vous ?"
		phrase2 = "Vous avez choisi cette attaque : "
		
	listeObjets = []
	
	with open(type, 'rb') as fichier:
		mon_depickler = pickle.Unpickler(fichier)
		try:
			while True:
				Objet = mon_depickler.load()
				listeObjets.append(Objet)
		except EOFError:
			pass
	
	if type == "attaques":
		listeObjets = [attaques for attaques in listeObjets if attaques.type.nom == typeAttaque.nom]
		if len(listeObjets) < 4:
			print("Il n'y a pas assez d'attaques de types " + typeAttaque.nom)
			return 0
	
	i = 0
	print('Voici les ' + type + ' dispos : ')
	while i < len(listeObjets):
		if type == "attaques":
			print(type, ' ', i + 1,' : ', listeObjets[i].nom, ' = ', listeObjets[i].degats)
		else:
			print(type, ' ', i + 1,' : ', listeObjets[i].nom)
		i += 1
	
	if type == "attaques":
		print("\nVous pouvez choisir 4 attaques parmis les dernières... Lesquelles choisissez-vous ? Entrez les numéros correspondants")
		i = 0
		attaquesChoisies = []
	
		while i < 4:
			print("Attaque", i + 1 , " : ")
			attaquesChoisies.append(creerVar("", 1, len(listeObjets)) - 1)
			i += 1
			
		print('Vous avez choisi les attaques : ')
		attaques = [listeObjets[attaquesChoisies[0]], listeObjets[attaquesChoisies[1]], listeObjets[attaquesChoisies[2]], listeObjets[attaquesChoisies[3]]]
		print(attaques[0].nom + " + " + attaques[1].nom + " + " + attaques[2].nom + " + " + attaques[3].nom)
		
		return attaques
	
	else:
		numObjet = creerVar(phrase, 1, len(listeObjets)) - 1
		ObjetChoisi = listeObjets[numObjet]
		print(phrase2, Objet.nom)
		return ObjetChoisi	

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

def toutSupprimer():
	""" Supprime tout """
	
	print("VOULEZ-VOUS VRAIMENT TOUT SUPPRIMER ? OUI = 1")
	rep = input("> ")
	if rep == "1":
		fichier = open('Types', 'w')
		fichier = open('attaques', 'w')
		fichier = open('Pokemons', 'w')
		fichier.close()
			
def supprimerChose(type):
	""" Supprime un objet """
	
	if nbChoses(type) == 0:
		print("Il n'y a pas de ", type)
	else:
		if type == "Pokemons":
			question = "Quel pokémon voulez-vous supprimer ?"
			reponse = "Ce pokémon n'existe pas."
			reponse2 = "Le pokémon a bien été supprimé."
		elif type == "Types":
			question = "Quel type voulez-vous supprimer ?"
			reponse = "Ce type n'existe pas."
			reponse2 = "Le type a bien été supprimé"
		else:
			question = "Quelle attaques voulez-vous supprimer ?"
			reponse = "Cette attaque n'existe pas."
			reponse2 = "L'attaque a bien été supprimée."
	
		rep = True
		while rep == True:
			print(question, " Tapez 1 pour voir la liste")
			nom = input('> ')
			if nom == "1":
				if type == "Pokemons":
					voirChose("Pokemons")
				elif type == "Types":
					voirChose("Types")
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
				
		print(reponse2)
			
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
