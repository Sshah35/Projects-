import json

from pygal.maps.world import World

#now we import the RotateStyle module

#pygal styles stored in style module

from pygal.style import RotateStyle

from pygal.style import LightColorizedStyle



# import our function get_country_code

from country_codes import get_country_code

#read the file population_data.json
filename="C:/python crash course/udemy/population_data.json"
with open(filename)as f1:
    loader=json.load(f1)

# build a dictionary for population data
    cc_population={}

#print the country name and the population of year 2010
for pop in loader:
    if pop["Year"]=="2010":
        country_name=pop["Country Name"]
        population=int(float(pop["Value"]))
        print("Country_name and Population based on year 2010\n ")
        print("country name is",country_name)
        print("population is",str(population))

# store the country code in a variable code

        code=get_country_code(country_name)

# country code is equal to the population
# population variable contain the Value which have the population of countries

        if code:
            cc_population[code]=population
            print("country code is:",code)

            if (pop["Country Name"]=="India" and (pop["Year"]=="2010")) :
                name=pop["Country Name"]
                pop1=pop["Value"]
                print("Country name is:",name)
                print("population is",pop1)

wm_style = RotateStyle('#445588')

wm = World(style=wm_style)

wm.title = 'World Population in 2010, by Country'
wm.add('2010', cc_population)
wm.render_to_file('world_population.svg')