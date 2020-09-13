
cars = ['Honda', 'BMW', 'Mercedes']

## Adding items to Lists
cars.append("Toyota")   #Added Toyota to end of list w/ .append

cars.insert(0 , "Fiat") #Added Fiat to position 0 w/ .insert
print (cars)

## Removing Items from Lists
del cars[2] #del removes the value of BMW
print (cars)

recent_purchase = cars.pop() #.pop removes the end of list item and retains the value
print (cars)
print ("The most recent thing I purchased was a " + recent_purchase)

too_expensive = "Mercedes"
cars.remove(too_expensive) #.remove uses the item name to delete it regardless of location
print (cars)
print(f"{too_expensive} is too expensive for me.")
