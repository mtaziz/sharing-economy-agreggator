#-*- coding:utf8 -*-

class France:
	def __init__(self):

		self.cities = [
					"Paris","Amiens","Nancy",
					"Rouen","Caen","Evreux","Saint Lo",
					"Rennes","Quimper","Morlaix","Vannes",
					"Strasbourg","Nantes","Clermont Ferrand",
					"Bordeaux","Dax","Chambery",
					"Poitiers","Perpignan","Nimes","Montpellier",
					"Marseille","Nice","Lyon","Toulouse","Limoges",
					"Besancon","Troyes","Orléans","Le mans","Gap","Millau",
					"Brives","Reims","Avallon","Le Puy en Velay","Aurillac",
					"Privas","Valence","Agen","Saint Brieuc","Cherbourg",
					"Charleville","Nevers","Angers","Pau"
					]

	def add_city(self, city):
		self.cities.append(city)
