#-*- coding:utf8 -*-
import re

def searchZip(str):
    pattern = re.compile("\d{5}")
    res = re.search(pattern, str)
    if res:
		return res.group()
    else:
		return 0    
class France:
	def __init__(self):

		self.cities = [
						"Paris","Marseille","Lyon","Toulouse","Nice","Nantes","Strasbourg","Montpellier","Bordeaux","Lille","Rennes",
						"Reims","Le Havre","Saint-Étienne","Toulon","Grenoble","Dijon","Angers","Nîmes","Villeurbanne","Saint-Denis",
						"Le Mans","Clermont-Ferrand","Aix-en-Provence","Brest","Limoges","Tours","Amiens","Perpignan","Metz","Boulogne-Billancourt","Besançon","Orléans","Rouen","Mulhouse","Caen","Saint-Denis","Nancy","Argenteuil","Saint-Paul","Montreuil","Roubaix","Tourcoing","Dunkerque","Nanterre","Créteil","Avignon","Vitry-sur-Seine","Poitiers",
						"Courbevoie","Fort-de-France","Versailles","Colombes","Asnières-sur-Seine","Aulnay-sous-Bois","Saint-Pierre",
						"Rueil-Malmaison","Pau","Aubervilliers","Champigny-sur-Marne","Le Tampon","Antibes","Saint-Maur-des-Fossés",
						"La Rochelle","Cannes","Béziers","Calais","Saint-Nazaire","Colmar","Drancy","Bourges","Mérignac","Ajaccio",
						"Issy-les-Moulineaux","Levallois-Perret","La Seyne-sur-Mer","Quimper","Noisy-le-Grand","Valence","Villeneuve-d'Ascq","Neuilly-sur-Seine","Antony","Vénissieux","Cergy","Troyes","Clichy","Pessac","Les Abymes","Ivry-sur-Seine",
						"Chambéry","Lorient","Niort","Sarcelles","Montauban","Villejuif","Saint-Quentin","Hyères","Cayenne","Épinay-sur-Seine","Saint-André","Beauvais","Maisons-Alfort","Cholet","Meaux","Chelles","Pantin","Fontenay-sous-Bois","La Roche-sur-Yon","Bondy","Vannes","Saint-Louis","Fréjus","Arles","Clamart","Évry","Le Blanc-Mesnil","Narbonne","Sartrouville","Grasse","Annecy","Laval","Belfort","Vincennes","Charleville-Mézières","Évreux",
						"Sevran","Albi","Montrouge","Bobigny","Martigues","Saint-Ouen","Brive-la-Gaillarde","Suresnes","Carcassonne","Cagnes-sur-Mer","Corbeil-Essonnes","Saint-Brieuc","Blois","Bayonne","Aubagne","Châlons-en-Champagne","Meudon","Châteauroux","Saint-Malo","Chalon-sur-Saône","Sète","Puteaux","Alfortville","Salon-de-Provence","Massy","Mantes-la-Jolie","Bastia","Vaulx-en-Velin","Saint-Herblain","Le Cannet","Valenciennes","Istres",
						"Gennevilliers","Boulogne-sur-Mer","Livry-Gargan","Saint-Priest","Rosny-sous-Bois","Caluire-et-Cuire","Angoulême",
						"Douai","Tarbes","Wattrelos","Castres","Choisy-le-Roi","Talence","Thionville","Arras","Alès","Garges-lès-Gonesse",
						"Gap","Saint-Laurent-du-Maroni","Melun","Bourg-en-Bresse","Noisy-le-Sec","Compiègne","La Courneuve","Le Lamentin",
						"Marcq-en-Barœul","Saint-Germain-en-Laye","Rezé","Bron","Anglet","Gagny","Chartres","Bagneux","Saint-Martin-d'Hères","Montluçon","Pontault-Combault","Poissy","Draguignan","Joué-lès-Tours","Savigny-sur-Orge","Cherbourg-Octeville","Saint-Joseph","Le Port","Colomiers","Saint-Martin","Villefranche-sur-Saône","Stains","Saint-Benoît",
						"Échirolles","Villepinte","Roanne","Montélimar","Saint-Chamond","Nevers","Moulins sur allier","Conflans-Sainte-Honorine","Auxerre","Sainte-Geneviève-des-Bois","Châtillon","Bagnolet","Vitrolles","Thonon-les-Bains","Neuilly-sur-Marne","Haguenau","Marignane","Saint-Raphaël","Tremblay-en-France","La Ciotat","Six-Fours-les-Plages","Creil","Agen","Romans-sur-Isère","Montigny-le-Bretonneux","Le Perreux-sur-Marne","Franconville","Annemasse",
						"Villeneuve-Saint-Georges","Saint-Leu","Mâcon","Cambrai","Lens","Houilles","Épinal","Châtenay-Malabry","Schiltigheim","Sainte-Marie","Liévin","Châtellerault","Meyzieu","Goussainville","Viry-Châtillon","Dreux",
						"L'Haÿ-les-Roses","Plaisir","Mont-de-Marsan","Maubeuge","Nogent-sur-Marne","Les Mureaux","Clichy-sous-Bois","La Possession","Dieppe","Chatou","Vandœuvre-lès-Nancy","Malakoff","Palaiseau","Pontoise","Charenton-le-Pont","Rillieux-la-Pape","Baie-Mahault","Saint-Laurent-du-Var","Athis-Mons","Périgueux","Trappes","Vienne","Sotteville-lès-Rouen",
						"Soissons","Saint-Étienne-du-Rouvray","Vallauris","Aurillac","Saumur","Vierzon","Alençon","Montbéliard","Biarritz",
						"Vichy","Saint-Dizier","Le Grand-Quevilly","Bruay-la-Buissière","Le Creusot","Orly","saint enimie","Meyrueis",
						"Mende","Saint chely","Millau","Rodez","auch","Porto Vecchio","Piana","Galeria","Saint Laurent du verdon","Vallon pont d'arc"
					]
		self.geo = {"Paris":{"lat":"48.86", "lon":"2.34445", "zipcode":"75001-75002-75003-75004-75005-75006-75007-75008-75009-75010-75011-75012-75013-75014-75015-75016-75017-75018-75019-75020-75116"}, "Marseille":{"lat":"43.2967", "lon":"5.37639", "zipcode": "13001-13002-13003-13004-13005-13006-13007-13008-13009-13010-13011-13012-13013-13014-13015-13016"},
					"Lyon":{"lat":"45.7589", "lon":"4.84139", "zipcode":"69001-69002-69003-69004-69005-69006-69007-69008-69009"}, "Toulouse":{"lat":"43.6", "lon":"1.43333","zipcode":"31000-31100-31200-31300-31400-31500"},
					"Nice":{"lat":"43.7", "lon":"7.25", "zipcode":"06000-06100-06200-06300"},"Nantes":{"lat":"47.2167", "lon":"-1.55","zipcode":"44000-44100-44200-44300"},
					"Strasbourg":{"lat":"48.5833", "lon":"7.75", "zipcode":"67000-67100-67200"},"Montpellier":{"lat":"43.6", "lon":"3.88333", "zipcode":"34000-34070-34080-34090"},
					"Bordeaux":{"lat":"44.8333", "lon":"-0.566667", "zipcode":"33000-33100-33200-33300-33800"},"Lille":{"lat":"50.6333", "lon":"3.06667","zipcode":"59000-59160-59260-59777-59800"},
					"Rennes":{"lat":"48.0833", "lon":"-1.68333", "zipcode":"35000-35200-35700"},"Reims":{"lat":"49.25", "lon":"4.03333","zipcode":"51100"},
					"Le Havre":{"lat":"49.5", "lon":"0.133333", "zipcode":"76600-76610-76620"},"Saint-Étienne":{"lat":"45.4333", "lon":"4.4", "zipcode":"42000-42100-42230"}}
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
