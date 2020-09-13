'''
6-8. Pets: Make several dictionaries, where each dictionary represents a differ-
ent pet. In each dictionary, include the kind of animal and the owner’s name.
Store these dictionaries in a list called pets . Next, loop through your list and as
you do, print everything you know about each pet.
'''
'''
pets = []
pet = {
    'name': 'mochi',
    'color': 'black and white',
    'age': 2,
    'size': 'small',
    'owner': 'eric',
    'type': 'dog'
}
pets.append(pet)
pet = {
    'name': 'bella',
    'color': 'brown',
    'age': 8,
    'size': 'small',
    'owner': 'gaby',
    'type': 'dog'
}
pets.append(pet)

for pet in pets:
    print(f"Here's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print('\t'+key.title() + ': ' + str(value))
'''
pets = []
mochi = {
    'name': 'mochi',
    'color': 'black and white',
    'age': 2,
    'size': 'small',
    'owner': 'eric',
    'type': 'dog'
}
pets.append(mochi)

bella = {
    'name': 'bella',
    'color': 'brown',
    'age': 8,
    'size': 'small',
    'owner': 'gaby',
    'type': 'dog'
}
pets.append(bella)

for pet in pets:
    print(f"Here's what I know about {pet['name'].title()}:")
    for key, value in pet.items():
        print('\t' + key + ': ' + str(value))
