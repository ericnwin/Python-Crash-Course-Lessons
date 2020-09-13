# Making Numerical Lists

# range() function prints a SERIES of numbers from (1, n) numbers
# ^ this will output numbers from (1 ,2 ,3... n-1)

for value in range(1, 6):
    print(value)

# if range(n) it'll start at 0 and count to n-1 numbers

# Making a list of # by using functions: list(range())

numbers = list(range(11))
print(numbers)

# can also use 3rd argument in range() to indicate step size

numbers2 = list(range(1, 6, 2))
print(numbers2)

# Squaring each number in list in a for loop
squares = []
for value in numbers2:
    square = value ** 2
    squares.append(square)
print(squares)

# can be more consise by combining line 24 with 25
squares = []
for value in numbers2:
    squares.append(value ** 2)
print(squares)

# Using LIST COMPREHENSION to shorten the code
squaress = [value**2 for value in range(1, 11)]
print(squaress)
# inside [(define expression for variable) for (variable) in (function)]
# notice the lack of colons for LIST COMPREHENSION
