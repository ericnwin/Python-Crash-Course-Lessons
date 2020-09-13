'''
8-6. City Names: Write a function called city_country() that takes in the name
of a city and its country. The function should return a string formatted like this:
"Santiago, Chile"
Call your function with at least three city-country pairs, and print the
values that are returned.
'''


def city_country(city, country):
    return f"{city.title()}, {country.title()}"


print(city_country('LA', 'America'))
print(city_country('seoul', 'korea'))
print(city_country('Moscow', 'Russia'))
