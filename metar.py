import requests
from lxml import etree

def parse_xml(metar, icao):
	working, symb = [], ['<', '>', '/', '\t', '\n']
	tree = metar.decode().split('metno:meteorologicalAerodromeReport')
	splitted = [_.split('metno:metarText') for _ in tree]
	for i in splitted:
		if type(i) == list:
			for j in i:
				if icao in j:
					working.append(j)
		else:
			if icao in i:
				working.append(i)

	raw_metar = working[-1]
	for i in symb:
		while i in raw_metar:
			raw_metar = raw_metar.replace(i, '')

	return raw_metar

def get_metar(icao):
	metar = requests.get(f'https://api.met.no/weatherapi/tafmetar/1.0/tafmetar.xml?icao={icao}')
	return parse_xml(metar.content, icao)
