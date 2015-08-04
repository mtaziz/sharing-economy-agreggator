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
					"Le Havre":{"lat":"49.5", "lon":"0.133333", "zipcode":"76600-76610-76620"},"Saint-Étienne":{"lat":"45.4333", "lon":"4.4", "zipcode":"42000-42100-42230"},
					"Toulon":{"lat":"43.1167", "lon":"5.93333", "zipcode":"83000-83100-83200"},"Grenoble":{"lat":"45.1667", "lon":"5.71667", "zipcode":"38000-38100"},
					"Dijon":{"lat":"47.3167", "lon":"5.01667", "zipcode":"21000-21100"},"Angers":{"lat":"47.4667", "lon":"47.4667", "zipcode":"49000-49100"},
					"Nîmes":{"lat":"43.8333", "lon":"4.35", "zipcode":"30000-30900"},"Villeurbanne":{"lat":"45.7667", "lon":"4.88333", "zipcode":"69100"},}
		self.geo_cities = {'Ch\xc3\xa2tellerault': {'lat': 46.8161209, 'lon': 0.5542895, 'zipcode': ''}, 'Sarcelles': {'lat': 48.9960813, 'lon': 2.3796245, 'zipcode': ''}, 'Cholet': {'lat': 47.0617293, 'lon': -0.8801349, 'zipcode': ''}, 'Lille': {'lat': 50.6305089, 'lon': 3.0706414, 'zipcode': ''}, 'Paris': {'lat': 48.8565056, 'lon': 2.3521334, 'zipcode': ''}, 'Saint-Malo': {'lat': 48.6454528, 'lon': -2.015418, 'zipcode': ''}, 'Martigues': {'lat': 43.4057279, 'lon': 5.0548176, 'zipcode': ''}, 'Biarritz': {'lat': 43.4815899, 'lon': -1.5561079, 'zipcode': ''}, 'Moulins sur allier': {'lat': 46.5613152, 'lon': 3.3389447, 'zipcode': ''}, 'S\xc3\xa8te': {'lat': 43.4017377, 'lon': 3.6941845, 'zipcode': ''}, 'Compi\xc3\xa8gne': {'lat': 49.4179497, 'lon': 2.8263171, 'zipcode': ''}, 'Piana': {'lat': 42.2388671, 'lon': 8.6370569, 'zipcode': ''}, 'Chamb\xc3\xa9ry': {'lat': 45.5662672, 'lon': 5.9203636, 'zipcode': ''}, 'Six-Fours-les-Plages': {'lat': 43.0935105, 'lon': 5.8393953, 'zipcode': ''}, 'Villefranche-sur-Sa\xc3\xb4ne': {'lat': 45.9864749, 'lon': 4.726611, 'zipcode': ''}, 'Malakoff': {'lat': 48.8174048, 'lon': 2.2971588, 'zipcode': ''}, 'Garges-l\xc3\xa8s-Gonesse': {'lat': 48.9703841, 'lon': 2.399024, 'zipcode': ''}, 'Nevers': {'lat': 46.9939033, 'lon': 3.1599641, 'zipcode': ''}, 'Courbevoie': {'lat': 48.8952393, 'lon': 2.2563404, 'zipcode': ''}, 'Asni\xc3\xa8res-sur-Seine': {'lat': 48.9105816, 'lon': 2.2890199, 'zipcode': ''}, 'Vitry-sur-Seine': {'lat': 48.7876, 'lon': 2.39164, 'zipcode': ''}, 'Villeneuve-Saint-Georges': {'lat': 48.7284955, 'lon': 2.4491931, 'zipcode': ''}, 'Bayonne': {'lat': 43.4933379, 'lon': -1.475099, 'zipcode': ''}, 'Aix-en-Provence': {'lat': 43.5298424, 'lon': 5.4474738, 'zipcode': ''}, 'Bondy': {'lat': 48.9031, 'lon': 2.48291, 'zipcode': ''}, 'Orly': {'lat': 48.7453214, 'lon': 2.3951433, 'zipcode': ''}, 'Saint-Herblain': {'lat': 47.2233007, 'lon': -1.6346964, 'zipcode': ''}, 'Trappes': {'lat': 48.7760957, 'lon': 1.9988356, 'zipcode': ''}, 'Nogent-sur-Marne': {'lat': 48.8353038, 'lon': 2.4810318, 'zipcode': ''}, 'M\xc3\xa2con': {'lat': 46.3036683, 'lon': 4.8322266, 'zipcode': ''}, 'Le Port': {'lat': -20.9354584, 'lon': 55.2916763, 'zipcode': ''}, 'Roanne': {'lat': 46.0363902, 'lon': 4.0738682, 'zipcode': ''}, 'Charenton-le-Pont': {'lat': 48.8219, 'lon': 2.40707, 'zipcode': ''}, 'Perpignan': {'lat': 42.6953868, 'lon': 2.8844713, 'zipcode': ''}, 'Mont-de-Marsan': {'lat': 43.8911318, 'lon': -0.500972, 'zipcode': ''}, 'Caen': {'lat': 49.1825099, 'lon': -0.367629, 'zipcode': ''}, 'Nantes': {'lat': 47.2185155, 'lon': -1.560235, 'zipcode': ''}, 'Goussainville': {'lat': 49.0323168, 'lon': 2.4733628, 'zipcode': ''}, 'Saint-Rapha\xc3\xabl': {'lat': 43.4255303, 'lon': 6.7694244, 'zipcode': ''}, 'Saumur': {'lat': 47.2597046, 'lon': -0.0778427, 'zipcode': ''}, 'Maisons-Alfort': {'lat': 48.8010363, 'lon': 2.4305233, 'zipcode': ''}, 'Chartres': {'lat': 48.4470039, 'lon': 1.4866387, 'zipcode': ''}, 'Saint chely': {'lat': 44.3137078, 'lon': 3.0581372, 'zipcode': ''}, 'Millau': {'lat': 44.1006693, 'lon': 3.0777594, 'zipcode': ''}, 'Thonon-les-Bains': {'lat': 46.3731303, 'lon': 6.4779448, 'zipcode': ''}, 'Colombes': {'lat': 48.922788, 'lon': 2.2543577, 'zipcode': ''}, "Vallon pont d'arc": {'lat': 44.4048, 'lon': 4.39289, 'zipcode': ''}, 'Poissy': {'lat': 48.9240863, 'lon': 2.03269486701654, 'zipcode': ''}, 'Livry-Gargan': {'lat': 48.917335, 'lon': 2.5298854, 'zipcode': ''}, 'M\xc3\xa9rignac': {'lat': 44.8422361, 'lon': -0.6469599, 'zipcode': ''}, 'Saint-Joseph': {'lat': 13.19763575, 'lon': -59.5454228478643, 'zipcode': ''}, '\xc3\x89pinay-sur-Seine': {'lat': 48.9525181, 'lon': 2.3145039, 'zipcode': ''}, 'Saint-Dizier': {'lat': 48.6375625, 'lon': 4.9475536, 'zipcode': ''}, 'Pontault-Combault': {'lat': 48.7884, 'lon': 2.61431, 'zipcode': ''}, 'saint enimie': {'lat': 44.3661054, 'lon': 3.4104994, 'zipcode': ''}, 'Marseille': {'lat': 43.2961743, 'lon': 5.3699525, 'zipcode': ''}, 'Champigny-sur-Marne': {'lat': 48.8183035, 'lon': 2.5146966, 'zipcode': ''}, 'Rosny-sous-Bois': {'lat': 48.8761957, 'lon': 2.4856366, 'zipcode': ''}, 'Boulogne-Billancourt': {'lat': 48.8356649, 'lon': 2.240206, 'zipcode': ''}, 'Villeurbanne': {'lat': 45.7733105, 'lon': 4.8869339, 'zipcode': ''}, 'La Ciotat': {'lat': 43.1758591, 'lon': 5.6062495, 'zipcode': ''}, 'Wattrelos': {'lat': 50.7008634, 'lon': 3.2222626, 'zipcode': ''}, 'Ch\xc3\xa2tillon': {'lat': 48.7997756, 'lon': 2.2897124, 'zipcode': ''}, 'Stains': {'lat': 48.9565669, 'lon': 2.3825154, 'zipcode': ''}, 'Mont\xc3\xa9limar': {'lat': 44.5579391, 'lon': 4.750318, 'zipcode': ''}, 'Le Lamentin': {'lat': 14.614557, 'lon': -61.0018145, 'zipcode': ''}, 'Saint-Quentin': {'lat': 49.8486111, 'lon': 3.2863888, 'zipcode': ''}, 'Niort': {'lat': 46.3239455, 'lon': -0.4645212, 'zipcode': ''}, 'Douai': {'lat': 50.3703683, 'lon': 3.0761377, 'zipcode': ''}, 'Vienne': {'lat': 48.2083537, 'lon': 16.3725042, 'zipcode': ''}, 'Rouen': {'lat': 49.4404591, 'lon': 1.0939658, 'zipcode': ''}, 'Clamart': {'lat': 48.800368, 'lon': 2.2630292, 'zipcode': ''}, 'Villejuif': {'lat': 48.7927, 'lon': 2.35845, 'zipcode': ''}, 'Saint-Laurent-du-Maroni': {'lat': 5.4987154, 'lon': -54.0305426, 'zipcode': ''}, 'Arles': {'lat': 43.6776223, 'lon': 4.6309653, 'zipcode': ''}, 'Saint-Martin': {'lat': 18.0814066, 'lon': -63.0467131, 'zipcode': ''}, "Villeneuve-d'Ascq": {'lat': 50.6271588, 'lon': 3.1506621, 'zipcode': ''}, 'Aulnay-sous-Bois': {'lat': 48.934231, 'lon': 2.499789, 'zipcode': ''}, 'Cambrai': {'lat': 50.1759602, 'lon': 3.2356613, 'zipcode': ''}, 'Vichy': {'lat': 46.1239268, 'lon': 3.4203712, 'zipcode': ''}, 'Strasbourg': {'lat': 48.584614, 'lon': 7.7507127, 'zipcode': ''}, 'Meyzieu': {'lat': 45.7764637, 'lon': 5.0044767, 'zipcode': ''}, 'Roubaix': {'lat': 50.6915893, 'lon': 3.1741734, 'zipcode': ''}, 'Melun': {'lat': 48.5353807, 'lon': 2.6591996, 'zipcode': ''}, 'Orl\xc3\xa9ans': {'lat': 47.9027336, 'lon': 1.9086066, 'zipcode': ''}, 'Bourges': {'lat': 47.0805693, 'lon': 2.398932, 'zipcode': ''}, 'Avignon': {'lat': 43.9493143, 'lon': 4.8060329, 'zipcode': ''}, 'Calais': {'lat': 50.9488, 'lon': 1.87468, 'zipcode': ''}, 'Palaiseau': {'lat': 48.7170283, 'lon': 2.2468567, 'zipcode': ''}, 'Choisy-le-Roi': {'lat': 48.7644619, 'lon': 2.4170727, 'zipcode': ''}, 'Creil': {'lat': 49.2635045, 'lon': 2.4737043, 'zipcode': ''}, 'Puteaux': {'lat': 48.8841522, 'lon': 2.2368863, 'zipcode': ''}, 'Aubervilliers': {'lat': 48.9146078, 'lon': 2.3821895, 'zipcode': ''}, 'Vierzon': {'lat': 47.2217489, 'lon': 2.0691421, 'zipcode': ''}, 'Narbonne': {'lat': 43.182806, 'lon': 3.0043128, 'zipcode': ''}, 'Dreux': {'lat': 48.7359121, 'lon': 1.3710486, 'zipcode': ''}, 'Cr\xc3\xa9teil': {'lat': 48.7830727, 'lon': 2.4518371, 'zipcode': ''}, 'Noisy-le-Sec': {'lat': 48.8905772, 'lon': 2.45468, 'zipcode': ''}, 'Le Blanc-Mesnil': {'lat': 48.9385489, 'lon': 2.4631476, 'zipcode': ''}, 'Reims': {'lat': 49.2577886, 'lon': 4.031926, 'zipcode': ''}, 'Rueil-Malmaison': {'lat': 48.8693888, 'lon': 2.1808837, 'zipcode': ''}, 'Drancy': {'lat': 48.9229821, 'lon': 2.4455201, 'zipcode': ''}, 'Ajaccio': {'lat': 41.9263991, 'lon': 8.7376029, 'zipcode': ''}, 'Montb\xc3\xa9liard': {'lat': 47.5102368, 'lon': 6.7977564, 'zipcode': ''}, 'La Seyne-sur-Mer': {'lat': 43.1007714, 'lon': 5.8788948, 'zipcode': ''}, 'Ch\xc3\xa2tenay-Malabry': {'lat': 48.7661105, 'lon': 2.2781646, 'zipcode': ''}, 'Pontoise': {'lat': 49.0508845, 'lon': 2.1008067, 'zipcode': ''}, 'Saint-Germain-en-Laye': {'lat': 48.8990413, 'lon': 2.0942792, 'zipcode': ''}, 'Alen\xc3\xa7on': {'lat': 48.4312059, 'lon': 0.0911374, 'zipcode': ''}, 'Anglet': {'lat': 43.4849503, 'lon': -1.5183409, 'zipcode': ''}, 'Rez\xc3\xa9': {'lat': 47.1905456, 'lon': -1.5695287, 'zipcode': ''}, '\xc3\x89chirolles': {'lat': 45.1437, 'lon': 5.71927, 'zipcode': ''}, 'Bourg-en-Bresse': {'lat': 46.2051192, 'lon': 5.2250324, 'zipcode': ''}, 'La Courneuve': {'lat': 48.9267236, 'lon': 2.3896123, 'zipcode': ''}, 'Saint-Laurent-du-Var': {'lat': 43.6690101, 'lon': 7.1906969, 'zipcode': ''}, 'Nice': {'lat': 43.7009358, 'lon': 7.2683912, 'zipcode': ''}, 'Grenoble': {'lat': 45.182478, 'lon': 5.7210773, 'zipcode': ''}, 'Boulogne-sur-Mer': {'lat': 50.7259985, 'lon': 1.6118771, 'zipcode': ''}, 'Istres': {'lat': 43.5139051, 'lon': 4.9884323, 'zipcode': ''}, 'Meudon': {'lat': 48.8126229, 'lon': 2.2387564, 'zipcode': ''}, 'Angers': {'lat': 47.4739884, 'lon': -0.5515588, 'zipcode': ''}, 'Aubagne': {'lat': 43.2924385, 'lon': 5.5703031, 'zipcode': ''}, 'Saint-Priest': {'lat': 45.6965347, 'lon': 4.9441635, 'zipcode': ''}, 'Beauvais': {'lat': 49.4409001, 'lon': 2.0866699, 'zipcode': ''}, 'Rodez': {'lat': 44.3510012, 'lon': 2.5733006, 'zipcode': ''}, 'Suresnes': {'lat': 48.8710147, 'lon': 2.2252883, 'zipcode': ''}, '\xc3\x89vry': {'lat': 48.6311001, 'lon': 2.438, 'zipcode': ''}, 'Le Havre': {'lat': 49.4938975, 'lon': 0.1079732, 'zipcode': ''}, 'N\xc3\xaemes': {'lat': 43.8374249, 'lon': 4.3600687, 'zipcode': ''}, 'auch': {'lat': 43.6464483, 'lon': 0.5847904, 'zipcode': ''}, 'Montrouge': {'lat': 48.8144, 'lon': 2.31606, 'zipcode': ''}, 'Mulhouse': {'lat': 47.7494188, 'lon': 7.3399355, 'zipcode': ''}, 'Carcassonne': {'lat': 43.2130358, 'lon': 2.3491069, 'zipcode': ''}, 'Sartrouville': {'lat': 48.9384, 'lon': 2.17761, 'zipcode': ''}, 'Saint-Beno\xc3\xaet': {'lat': 43.9673239, 'lon': 6.7254961, 'zipcode': ''}, 'Hy\xc3\xa8res': {'lat': 43.1202573, 'lon': 6.1301614, 'zipcode': ''}, 'Montreuil': {'lat': 50.463745, 'lon': 1.7642283, 'zipcode': ''}, 'Chalon-sur-Sa\xc3\xb4ne': {'lat': 46.7888997, 'lon': 4.8529605, 'zipcode': ''}, 'Alfortville': {'lat': 48.7928634, 'lon': 2.4277061, 'zipcode': ''}, 'La Roche-sur-Yon': {'lat': 46.6705431, 'lon': -1.4269698, 'zipcode': ''}, 'Mantes-la-Jolie': {'lat': 48.9891971, 'lon': 1.7140683, 'zipcode': ''}, 'Metz': {'lat': 49.1196964, 'lon': 6.1763552, 'zipcode': ''}, 'Bagneux': {'lat': 49.458056, 'lon': 3.279444, 'zipcode': ''}, 'Saint Laurent du verdon': {'lat': 43.7244469, 'lon': 6.0681209, 'zipcode': ''}, 'Le Perreux-sur-Marne': {'lat': 48.8406703, 'lon': 2.5080558, 'zipcode': ''}, 'Agen': {'lat': 44.2015624, 'lon': 0.6176324, 'zipcode': ''}, 'Bron': {'lat': 45.7337532, 'lon': 4.9092352, 'zipcode': ''}, 'Tours': {'lat': 47.3900474, 'lon': 0.6889268, 'zipcode': ''}, 'Grasse': {'lat': 43.6589011, 'lon': 6.9239103, 'zipcode': ''}, 'Corbeil-Essonnes': {'lat': 48.6137682, 'lon': 2.4803415, 'zipcode': ''}, 'Bagnolet': {'lat': 48.8688199, 'lon': 2.4173658, 'zipcode': ''}, 'Fontenay-sous-Bois': {'lat': 48.8508, 'lon': 2.47251, 'zipcode': ''}, 'Li\xc3\xa9vin': {'lat': 50.4245, 'lon': 2.7738, 'zipcode': ''}, 'Lyon': {'lat': 45.7575286, 'lon': 4.8324803, 'zipcode': ''}, 'Caluire-et-Cuire': {'lat': 45.7969952, 'lon': 4.8423304, 'zipcode': ''}, 'La Rochelle': {'lat': 46.1591126, 'lon': -1.1520434, 'zipcode': ''}, 'Pessac': {'lat': 44.8055629, 'lon': -0.6302789, 'zipcode': ''}, 'B\xc3\xa9ziers': {'lat': 43.341279, 'lon': 3.2166203, 'zipcode': ''}, 'Cayenne': {'lat': 4.9371143, 'lon': -52.3258307, 'zipcode': ''}, 'Meyrueis': {'lat': 44.1803, 'lon': 3.43056, 'zipcode': ''}, 'Sotteville-l\xc3\xa8s-Rouen': {'lat': 49.4151549, 'lon': 1.089746, 'zipcode': ''}, 'Savigny-sur-Orge': {'lat': 48.6842593, 'lon': 2.3482788, 'zipcode': ''}, 'Galeria': {'lat': 42.4084817, 'lon': 8.647919, 'zipcode': ''}, 'Annecy': {'lat': 45.8977758, 'lon': 6.1333989, 'zipcode': ''}, "L'Ha\xc3\xbf-les-Roses": {'lat': 48.7776577, 'lon': 2.3369786, 'zipcode': ''}, 'Belfort': {'lat': 47.6379599, 'lon': 6.8628942, 'zipcode': ''}, 'Gap': {'lat': 44.5611978, 'lon': 6.0820018, 'zipcode': ''}, 'V\xc3\xa9nissieux': {'lat': 45.7036, 'lon': 4.88079, 'zipcode': ''}, 'Troyes': {'lat': 48.2971626, 'lon': 4.0746257, 'zipcode': ''}, 'Lens': {'lat': 50.4291723, 'lon': 2.8319805, 'zipcode': ''}, 'Cherbourg-Octeville': {'lat': 49.6292405, 'lon': -1.6384497, 'zipcode': ''}, 'Conflans-Sainte-Honorine': {'lat': 49.0003001, 'lon': 2.1017799, 'zipcode': ''}, 'Sainte-Marie': {'lat': 47.5091856, 'lon': 6.6967773, 'zipcode': ''}, 'Saint-Paul': {'lat': 43.6941, 'lon': 7.12264, 'zipcode': ''}, 'Gennevilliers': {'lat': 48.9254221, 'lon': 2.2940122, 'zipcode': ''}, 'Cagnes-sur-Mer': {'lat': 43.6612012, 'lon': 7.1513834, 'zipcode': ''}, 'Baie-Mahault': {'lat': 16.2679458, 'lon': -61.5870766, 'zipcode': ''}, 'Saint-Denis': {'lat': 48.935773, 'lon': 2.3580232, 'zipcode': ''}, 'Le Mans': {'lat': 48.0077781, 'lon': 0.1995339, 'zipcode': ''}, 'Argenteuil': {'lat': 48.9479069, 'lon': 2.2481797, 'zipcode': ''}, 'Vaulx-en-Velin': {'lat': 45.7784255, 'lon': 4.9206153, 'zipcode': ''}, 'Saint-Maur-des-Foss\xc3\xa9s': {'lat': 48.8005783, 'lon': 2.4949924, 'zipcode': ''}, 'Blois': {'lat': 47.5876861, 'lon': 1.3337639, 'zipcode': ''}, 'Saint-Chamond': {'lat': 45.4748298, 'lon': 4.5098046, 'zipcode': ''}, 'Saint-Andr\xc3\xa9': {'lat': -20.9606333, 'lon': 55.6492731, 'zipcode': ''}, 'Meaux': {'lat': 48.9589146, 'lon': 2.8964865, 'zipcode': ''}, 'Albi': {'lat': 43.9277552, 'lon': 2.147899, 'zipcode': ''}, 'Vitrolles': {'lat': 43.4593696, 'lon': 5.2482643, 'zipcode': ''}, 'Montlu\xc3\xa7on': {'lat': 46.3399276, 'lon': 2.6067229, 'zipcode': ''}, 'Tremblay-en-France': {'lat': 48.9802035, 'lon': 2.5589558, 'zipcode': ''}, 'Dijon': {'lat': 47.3215806, 'lon': 5.0414701, 'zipcode': ''}, 'Les Abymes': {'lat': 16.2706436, 'lon': -61.5057749, 'zipcode': ''}, 'Clichy': {'lat': 48.9026, 'lon': 2.30551, 'zipcode': ''}, 'Dieppe': {'lat': 49.9246182, 'lon': 1.0791444, 'zipcode': ''}, 'Jou\xc3\xa9-l\xc3\xa8s-Tours': {'lat': 47.3510905, 'lon': 0.6622524, 'zipcode': ''}, 'Athis-Mons': {'lat': 48.7079028, 'lon': 2.3890941, 'zipcode': ''}, 'Montigny-le-Bretonneux': {'lat': 48.7759215, 'lon': 2.0249424, 'zipcode': ''}, 'Rillieux-la-Pape': {'lat': 45.823514, 'lon': 4.8994366, 'zipcode': ''}, 'Colomiers': {'lat': 43.6121001, 'lon': 1.3282149, 'zipcode': ''}, 'Fr\xc3\xa9jus': {'lat': 43.4330308, 'lon': 6.7360182, 'zipcode': ''}, 'Cannes': {'lat': 43.5512076, 'lon': 7.0126946, 'zipcode': ''}, 'P\xc3\xa9rigueux': {'lat': 45.1909365, 'lon': 0.7184407, 'zipcode': ''}, 'Bordeaux': {'lat': 44.841225, 'lon': -0.5800364, 'zipcode': ''}, 'Valence': {'lat': 44.9332277, 'lon': 4.8920811, 'zipcode': ''}, 'Talence': {'lat': 44.8088438, 'lon': -0.5879629, 'zipcode': ''}, 'Ivry-sur-Seine': {'lat': 48.8122302, 'lon': 2.3872525, 'zipcode': ''}, 'Gagny': {'lat': 48.8842139, 'lon': 2.5321482, 'zipcode': ''}, 'Nanterre': {'lat': 48.8924273, 'lon': 2.2071267, 'zipcode': ''}, 'Toulouse': {'lat': 43.6044622, 'lon': 1.4442469, 'zipcode': ''}, 'Thionville': {'lat': 49.3591614, 'lon': 6.1529769, 'zipcode': ''}, 'Amiens': {'lat': 49.8941708, 'lon': 2.2956951, 'zipcode': ''}, 'Antibes': {'lat': 43.5836, 'lon': 7.10905, 'zipcode': ''}, 'Le Cannet': {'lat': 43.6130556, 'lon': -0.0522222, 'zipcode': ''}, 'Ch\xc3\xa2lons-en-Champagne': {'lat': 48.9566218, 'lon': 4.3628851, 'zipcode': ''}, 'Pantin': {'lat': 48.8965023, 'lon': 2.4019804, 'zipcode': ''}, 'Cergy': {'lat': 49.0527528, 'lon': 2.0388736, 'zipcode': ''}, 'Clichy-sous-Bois': {'lat': 48.910939, 'lon': 2.5460722, 'zipcode': ''}, 'Marcq-en-Bar\xc5\x93ul': {'lat': 50.6767018, 'lon': 3.1043032, 'zipcode': ''}, 'Brest': {'lat': 48.3905283, 'lon': -4.4860088, 'zipcode': ''}, 'Fort-de-France': {'lat': 14.6037193, 'lon': -61.0767677, 'zipcode': ''}, 'Neuilly-sur-Marne': {'lat': 48.8642, 'lon': 2.53921, 'zipcode': ''}, 'Pau': {'lat': 43.2957547, 'lon': -0.3685668, 'zipcode': ''}, 'Annemasse': {'lat': 46.1934005, 'lon': 6.2341093, 'zipcode': ''}, 'Saint-Ouen': {'lat': 48.911729, 'lon': 2.334267, 'zipcode': ''}, 'Valenciennes': {'lat': 50.3594889, 'lon': 3.5266657, 'zipcode': ''}, 'Saint-Leu': {'lat': -21.1677694, 'lon': 55.2881932, 'zipcode': ''}, 'Besan\xc3\xa7on': {'lat': 47.237953, 'lon': 6.0243246, 'zipcode': ''}, 'Massy': {'lat': 48.7282317, 'lon': 2.2735978, 'zipcode': ''}, 'Toulon': {'lat': 43.1257311, 'lon': 5.9304919, 'zipcode': ''}, 'Saint-Brieuc': {'lat': 48.5141594, 'lon': -2.7602707, 'zipcode': ''}, 'Villepinte': {'lat': 48.9636566, 'lon': 2.5347541, 'zipcode': ''}, 'Aurillac': {'lat': 44.9285441, 'lon': 2.4433101, 'zipcode': ''}, 'Chatou': {'lat': 48.8987, 'lon': 2.15122, 'zipcode': ''}, 'Soissons': {'lat': 49.3816667, 'lon': 3.3236111, 'zipcode': ''}, 'Les Mureaux': {'lat': 48.9958047, 'lon': 1.9090697, 'zipcode': ''}, 'Franconville': {'lat': 48.9890001, 'lon': 2.2247099, 'zipcode': ''}, 'Versailles': {'lat': 48.8035403, 'lon': 2.1266886, 'zipcode': ''}, 'Clermont-Ferrand': {'lat': 45.7774551, 'lon': 3.0819427, 'zipcode': ''}, '\xc3\x89vreux': {'lat': 49.0183639, 'lon': 1.1375865, 'zipcode': ''}, 'Brive-la-Gaillarde': {'lat': 45.1584982, 'lon': 1.5332389, 'zipcode': ''}, 'Auxerre': {'lat': 47.7954001, 'lon': 3.58452, 'zipcode': ''}, 'Houilles': {'lat': 48.926, 'lon': 2.18709, 'zipcode': ''}, 'Vincennes': {'lat': 48.8474508, 'lon': 2.4396714, 'zipcode': ''}, 'Saint-Louis': {'lat': 16.187637, 'lon': -15.2954315, 'zipcode': ''}, 'Saint-\xc3\x89tienne-du-Rouvray': {'lat': 49.3831, 'lon': 1.09163, 'zipcode': ''}, 'Dunkerque': {'lat': 51.0347708, 'lon': 2.3772525, 'zipcode': ''}, 'Quimper': {'lat': 47.9960325, 'lon': -4.1024782, 'zipcode': ''}, 'Le Tampon': {'lat': -21.2776484, 'lon': 55.5157955, 'zipcode': ''}, 'Al\xc3\xa8s': {'lat': 44.1253665, 'lon': 4.0852818, 'zipcode': ''}, 'Castres': {'lat': 43.6036776, 'lon': 2.2417954, 'zipcode': ''}, 'Neuilly-sur-Seine': {'lat': 48.884683, 'lon': 2.2695658, 'zipcode': ''}, 'Mende': {'lat': 44.5180226, 'lon': 3.4991057, 'zipcode': ''}, 'Maubeuge': {'lat': 50.2785567, 'lon': 3.9743784, 'zipcode': ''}, 'Colmar': {'lat': 48.0777517, 'lon': 7.3579641, 'zipcode': ''}, 'Bobigny': {'lat': 48.906387, 'lon': 2.4452231, 'zipcode': ''}, 'Le Creusot': {'lat': 46.808203, 'lon': 4.4297028, 'zipcode': ''}, 'Schiltigheim': {'lat': 48.6076873, 'lon': 7.7500608, 'zipcode': ''}, 'Viry-Ch\xc3\xa2tillon': {'lat': 48.6695097, 'lon': 2.3732542, 'zipcode': ''}, 'La Possession': {'lat': -20.9269658, 'lon': 55.3361334, 'zipcode': ''}, 'Lorient': {'lat': 47.7504, 'lon': -3.37958, 'zipcode': ''}, 'Chelles': {'lat': 48.8797422, 'lon': 2.5942129, 'zipcode': ''}, 'Saint-Pierre': {'lat': -21.341298, 'lon': 55.4776174, 'zipcode': ''}, 'Noisy-le-Grand': {'lat': 48.8493972, 'lon': 2.5519571, 'zipcode': ''}, 'Saint-Nazaire': {'lat': 45.2566002, 'lon': 5.8490243, 'zipcode': ''}, 'Vannes': {'lat': 47.6586772, 'lon': -2.7599079, 'zipcode': ''}, 'Ch\xc3\xa2teauroux': {'lat': 46.8047, 'lon': 1.6957099, 'zipcode': ''}, 'Porto Vecchio': {'lat': 41.5921091, 'lon': 9.2761531, 'zipcode': ''}, 'Draguignan': {'lat': 43.5398458, 'lon': 6.4655798, 'zipcode': ''}, 'Le Grand-Quevilly': {'lat': 49.4068986, 'lon': 1.0507926, 'zipcode': ''}, 'Saint-\xc3\x89tienne': {'lat': 45.4401467, 'lon': 4.3873058, 'zipcode': ''}, 'Nancy': {'lat': 48.6928048, 'lon': 6.1838123, 'zipcode': ''}, 'Vand\xc5\x93uvre-l\xc3\xa8s-Nancy': {'lat': 48.6574993, 'lon': 6.1653957, 'zipcode': ''}, 'Vallauris': {'lat': 43.5761001, 'lon': 7.05859, 'zipcode': ''}, 'Rennes': {'lat': 48.1113589, 'lon': -1.680009, 'zipcode': ''}, 'Antony': {'lat': 48.753554, 'lon': 2.2959423, 'zipcode': ''}, 'Limoges': {'lat': 45.8354243, 'lon': 1.2644847, 'zipcode': ''}, '\xc3\x89pinal': {'lat': 48.1745644, 'lon': 6.4506416, 'zipcode': ''}, 'Plaisir': {'lat': 48.817399, 'lon': 1.9476363, 'zipcode': ''}, 'Romans-sur-Is\xc3\xa8re': {'lat': 45.0458886, 'lon': 5.0528681, 'zipcode': ''}, 'Montpellier': {'lat': 43.6112422, 'lon': 3.8767337, 'zipcode': ''}, 'Angoul\xc3\xaame': {'lat': 45.6496755, 'lon': 0.1568658, 'zipcode': ''}, 'Levallois-Perret': {'lat': 48.8951087, 'lon': 2.2873009, 'zipcode': ''}, "Saint-Martin-d'H\xc3\xa8res": {'lat': 45.1840758, 'lon': 5.7539023, 'zipcode': ''}, 'Poitiers': {'lat': 46.5802596, 'lon': 0.340196, 'zipcode': ''}, 'Haguenau': {'lat': 48.8172236, 'lon': 7.7885978, 'zipcode': ''}, 'Montauban': {'lat': 44.0175835, 'lon': 1.3549991, 'zipcode': ''}, 'Arras': {'lat': 50.2912099, 'lon': 2.7771364, 'zipcode': ''}, 'Marignane': {'lat': 43.4162729, 'lon': 5.2146275, 'zipcode': ''}, 'Sainte-Genevi\xc3\xa8ve-des-Bois': {'lat': 48.6424322, 'lon': 2.3283953, 'zipcode': ''}, 'Tarbes': {'lat': 43.232858, 'lon': 0.0781021, 'zipcode': ''}, 'Tourcoing': {'lat': 50.7217304, 'lon': 3.1593082, 'zipcode': ''}, 'Bastia': {'lat': 42.7065505, 'lon': 9.452542, 'zipcode': ''}, 'Laval': {'lat': 48.0710377, 'lon': -0.7723499, 'zipcode': ''}, 'Issy-les-Moulineaux': {'lat': 48.8250508, 'lon': 2.273457, 'zipcode': ''}, 'Bruay-la-Buissi\xc3\xa8re': {'lat': 50.4919, 'lon': 2.55377, 'zipcode': ''}, 'Sevran': {'lat': 48.9372068, 'lon': 2.5289296, 'zipcode': ''}, 'Charleville-M\xc3\xa9zi\xc3\xa8res': {'lat': 49.7599365, 'lon': 4.7186932, 'zipcode': ''}, 'Salon-de-Provence': {'lat': 43.6405308, 'lon': 5.0980217, 'zipcode': ''}}

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
