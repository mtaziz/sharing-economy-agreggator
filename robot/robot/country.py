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
					"Annecy","Thonon les bains","Albertville","Briancon",
					"Carcasonne","Narbonne","Mimizan","Arcachon","Bergerac","Saintes", 
					"Tours","Chateau-Thierry","Saint Malo","Loudeac","Carhaix","brest",
					"Laval","Le Mans","Dreux","Charleville"
					]

	def add_city(self, city):
		self.cities.append(city)

	def city_from_title(self, title):
		for city in self.cities:
			if city in title:
				return city
class Spain:
	def __init__(self):

		self.cities = [
					"Madrid","Barcelone","Valence",
					"Séville","Bilbao","Malaga","Asturies",
					"Alicante","Murcie","Las Palmas de Gran Canaria"
					]

	def add_city(self, city):
		self.cities.append(city)