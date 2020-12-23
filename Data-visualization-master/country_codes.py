from pygal.maps.world import COUNTRIES

def get_country_code(country_name):
    """Return the Pygal 2-digit country code for the given country."""
    for code, name in COUNTRIES.items():
        if name == country_name:
            return code
    # If the country wasn't found, return None.
    return None

# print the country codes of few countries as a sample
print(get_country_code("Andorra"))
print(get_country_code("Arab World"))
print(get_country_code("Caribbean small states"))
print(get_country_code('United Arab Emirates'))
print(get_country_code('Afghanistan'))
print(get_country_code("Canada"))

#Asian countries
print("\t\t\tAsian countries\t\t\t \n")

print("India",get_country_code("India"))
print("Japan",get_country_code("Japan"))
print("China",get_country_code("China"))
print("Indonesia",get_country_code("Indonesia"))
print("Thailand",get_country_code("Thailand"))
print("Singapore",get_country_code("Singapore"))


#Arab countries
print("\t\t\tArab countries\t\t\t \n")

print("Egypt",get_country_code("Egypt"))
print("Iraq",get_country_code("Iraq"))
print("Algeria",get_country_code("Algeria"))
print("Bahrain",get_country_code("Bahrain"))
print("Jordan",get_country_code("Jordan"))
print("Saudi Arabia",get_country_code("Saudi Arabia"))
print("Syria",get_country_code("Syria"))
print("United Arab Emirates",get_country_code("United Arab Emirates"))

print(get_country_code("North America"))