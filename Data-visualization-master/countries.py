import pygal

#Population_data.json file have 3 digit country code but

#pygal accept 2 digit country codes, So we have to import a module for 2 digit country code

# import module COUNTRIES

# pygal country codes are stored in a module COUNTRIES

# COUNTRIES have the two digit country codes

from pygal.maps.world import COUNTRIES

for country_code in sorted(COUNTRIES.keys()):
    print(country_code, COUNTRIES[country_code])
