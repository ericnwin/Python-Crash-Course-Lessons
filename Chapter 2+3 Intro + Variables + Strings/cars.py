# Organizing a list w/ .sort() and .sorted()

cars = ['audi', 'bmw', 'toyota', 'honda', 'mercedes']
# cars.sort()  ## sort() modifies the list permanently alphabetically
# print(cars)

# cars.sort(reverse=True) ## sort(reverse=True) sets the list to reverse alphabetical order
# print(cars)

# Using sort() to temporarily organize list keeping original list
print("Here is the original list:")
print(cars)

print("\nHere's the sorted list:")
print(sorted(cars))

print("\nHere is the orginal list again:")
print(cars)

# can also use sort(reverse=True) to sort reverse alphabetically

# Printing a list in Reverse Order (NOT ALPHABETICALLY)

fav_food = ['ramen', 'poke', 'dogs', 'pasta']
print(fav_food)

fav_food.reverse()
print(fav_food)  # .reverse() modifies list permanently
# Can use .reverse again to get original list tho

# Use len() to find Length of list
print(len(fav_food))

# Very useful!! can be used to determine # of registered users on a website
# or # of aliens shot in a game
