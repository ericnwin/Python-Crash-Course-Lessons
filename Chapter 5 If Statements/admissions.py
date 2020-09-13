# Using if-elif-else statements for an amusement park scenario

# if-elif-else statements test for only one condition then executes that portion of code. in essence if you need one test to pass use if-elif-else statement
# if you need multiple tests, use multiple if statements!
'''
if the person is:
    under age of 4 = price is free
    pre-18 = price is $10
    18 or older = senior pricing of $25
    65+ = price is $25
'''
age = 65

if age < 4:
    price = 0
elif age < 18:
    price = 10
elif age < 65:
    price = 50
else:
    price = 25

print(f'Please pay {price}')

# the else part will only be executed if age is over 65
