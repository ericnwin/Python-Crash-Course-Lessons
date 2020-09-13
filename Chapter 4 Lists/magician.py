# Intro to for loops

magicians = ['donna', 'magnifico', 'alabaster']
for variable in magicians:
    print(f'{variable.title()}, how\'d you do that trick?')
    print(
        f'I\'m actually really looking forward to your next trick, {variable.title()}!\n')
# associate the list magicians to the variable
# and then print out each name in variable

# How for loops work

# Python reads the 1st line the for loop
# then associates the 1st value in the magicians list to variable
# looks at print(variable) and executes it
# because there's more values in our list magician
# Python goes back and grabs 2nd value and executes print(variable) again
# repeats until all values have been executes with print(varaible)
# Python then goes on to the next line in the for loop
# in our case there isn't anything

# Basically Python executes the code for each individual item in the list
# then executes it with the next one on the list
