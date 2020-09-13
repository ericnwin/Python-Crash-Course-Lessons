
x, y, z = "poop", "hehe", "doodoo"
print(x)
print(y)
print(z)

# Capital = Constants!
MAX_PEOPLE = "a"

cars = ['Honda', 'BMW', 'Mercedes']
print(cars[1])

# Add items to our list

japanese = "Toyota"
cars.insert(0, japanese)
print(cars)

# Removing Items from our list

del(cars[1])  # del = removing the value + object
print(cars)

# pop = removing the object, but NOT the value from last item on list
car_i_dont_want = cars.pop()
print(cars)
print(car_i_dont_want)

cars.append("BMW")
print(cars)
cars.remove("BMW")
cars.remove("BMW")
print(cars)
'''
cars = cars.append('audi')
print(cars)
cars.append('subaru')
cars.append('bmw')
print(cars)
'''

print(int(2.777))

ticket = "090234"
print(ticket[0])
print([int(i) for i in ticket])
