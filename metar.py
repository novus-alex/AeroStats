import requests

def parse_xml(metar, icao):
	splitted = metar.split(icao)
	print(splitted)


def get_metar(icao):
	metar = requests.get(f'https://api.met.no/weatherapi/tafmetar/1.0/tafmetar.xml?icao={icao}')
	return parse_xml(metar.content, icao)

print(get_metar('LFMN'))