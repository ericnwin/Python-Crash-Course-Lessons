'''
10-11. Favorite Number: Write a program that prompts for the user’s favorite
number. Use json.dump() to store this number in a file. Write a separate pro-
gram that reads in this value and prints the message, “I know your favorite
number! It’s _____.”
'''
import json

fav_number = input("whats your favorite number?")

file_name = 'fav_number.json'

with open(file_name, 'w') as f:
    json.dump(fav_number, f)
