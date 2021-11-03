import requests
import pandas as pd

def get_species_data_from_specieslink(species_name, file):
	''' Returns pandas DataFrame with all information about the species from SpeciesLink'''
	assert species_name != 0, 'Must provide species name'
	assert file != 0, 'Must provide destination csv file'
	endereco = 'https://api.splink.org.br/records/ScientificName/' + species_name + '/format/json'
	r = requests.get(endereco)
	assert r.status_code == 200, 'Connection to SpeciesLink failed'
	r = r.json()
	r = r['result']
	r = pd.DataFrame.from_dict(r)
	r.rename(columns={'decimalLongitude':'lon', 'decimalLatitude':'lat'}, inplace=True)
	r.to_csv(file)
	return r

def write_kml(file="/Users/tiagopires/Desktop/temp.kml", dataframe):
	''' Write KML file with sampling points coordinates of the species from the dataframe loaded using get_species_data_from_specieslink() '''
	if not 'lon' in dataframe.columns:
		'Precisa de colunas lat e lon que representam as coordenadas'
	dataframe.dropna(subset=['lat','lon'], inplace=True) 
	dataframe.reset_index(inplace=True)	
	f = open(file, "a")
	f.write('<?xml version="1.0" encoding="UTF-8"?><kml xmlns="http://www.opengis.net/kml/2.2" xmlns:gx="http://www.google.com/kml/ext/2.2" xmlns:kml="http://www.opengis.net/kml/2.2" xmlns:atom="http://www.w3.org/2005/Atom"><Document>')
	for i in range(dataframe.shape[0]):
		coords = dataframe.lon[i] + ',' + dataframe.lat[i]
		sp = dataframe.scientificName[i]
		block = '<Placemark>\
		<name>' + sp + '</name>\
		<styleUrl>#m_ylw-pushpin</styleUrl>\
		<Point>\
		<gx:drawOrder>1</gx:drawOrder>\
		<coordinates>' + coords + '</coordinates>\
		</Point>\
		</Placemark>'
		f.write(block)
	f.write('</Document></kml>')
	f.close()

r = get_species_data_from_specieslink(species_name='Phalloceros harpagos', file='~/Desktop/temp.csv')
write_kml(dataframe=r)
