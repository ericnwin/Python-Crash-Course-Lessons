'''
6-11. Cities: Make a dictionary called cities . Use the names of three cities as
keys in your dictionary. Create a dictionary of information about each city and
include the country that the city is in, its approximate population, and one fact
about that city. The keys for each city’s dictionary should be something like
country , population , and fact . Print the name of each city and all of the infor-
mation you have stored about it.
'''

cities = {
    'los angeles': {
        'country': 'america',
        'fact': 'LA is the center of the film and TV industry',
        'population': 10_000_000,
    },
    'seoul': {
        'country': 'korea',
        'fact': 'Korea is home to yummy food and has the fastest internet',
        'population': 9_700_000,
    },
    'london': {
        'country': 'united kingdom',
        'fact': "London's citizens are a big supporter of Indian cuisine",
        'population': 9_000_000,
    },
}

for city, city_info in cities.items():
    country = city_info['country']
    fact = city_info['fact']
    population = city_info['population']
    print(f"{city.title()} is in " + country.title())
    print(f"\tA cool fact about {city.title()} is that " + fact)
    print(f"\tAnd the population of {city.title()} is " + str(population))

# changing a key entry into a new one, effectively replacing the old key - london with the new key - tokyo
cities['tokyo'] = cities['london']
del cities['london']
print(cities)
