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
					"Charleville","Nevers","Angers","Pau",
					"Lille","calais","Moulins","Chateauroux","Chartres",
					"Angouleme","Chateaubriant","Pontivy","chaumont","Mulhouse",
					"Mende","Saint flour","Nyons","Digne","Draguignan","Grenoble",
					"Auch","Foix","Bagnères de Luchon","Castres","Albi","Cahors",
					"Rodez","La rochelle","Chalon sur Saone","Dijon","Manosque","Frejus",
					"Annecy","Thonon les bains","Albertville","Briancon"
					]

	def add_city(self, city):
		self.cities.append(city)