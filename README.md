# specieslink
Get some data from SpeciesLink API for later processing
Can retrieve all information of a given species using genus + epithet ("Genus speciesname") and load as pandas DataFrame
  - Changes 'decimalLongitude' to 'lon' and 'decimalLatitude' to 'lat'
Can write a KML file using 'lat' and 'lon' columns of a dataframe such as the one from get_species_data_from_specieslink()
# --- Plenty of work still to be done, but functional
