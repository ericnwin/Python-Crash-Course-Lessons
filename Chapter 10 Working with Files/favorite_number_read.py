import json

with open('fav_number.json', 'r') as f:
    number = json.load(f)

print("I know your favorite number! It's ", str(number), '!')
