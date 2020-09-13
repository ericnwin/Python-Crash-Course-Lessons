'''
9-14. Lottery: Make a list or tuple containing a series of 10 numbers and
five letters. Randomly select four numbers or letters from the list and print a
message saying that any ticket matching these four numbers or letters wins a
prize.
'''
import random

import string

letters = string.ascii_lowercase
print(letters)  # returns abcdefg....xyz
list_letters = ''.join(random.choice(letters) for i in range(5))
# returns a random list of 5 letters

list_numbers = [random.randint(1, 50) for i in range(10)]
# return a random list of 10 letters
list_numbers.extend(list_letters)  # adding list 1 and list 2 together
#   random.shuffle(list_numbers)
print(list_numbers)

print("The winning ticket is:", random.choices(list_numbers, k=4))

# choice returns rand single element from list tuple etc
# choices returns rand element with k sized list
