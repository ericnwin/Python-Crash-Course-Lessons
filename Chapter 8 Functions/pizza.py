'''
using def function(*parameter) to make a tuple
that outputs any value it receives into that tuple.
THIS IS USEFUL IF YOU DON'T KNOW THE # OF ARGUMENTS
YOUR FUNCTION WILL USE 
'''


def make_pizza(*toppings):
    print(toppings)


make_pizza('mushroom', 'pepperoni', 'bell pepper')
make_pizza('cheese')

'''
positional parameter must come before 'arbitrary' argument
Python will match it up -> super easy!!
'''


def make_pizza2(size, *toppings):
    print(f"Making {size} inch pizza!")
    print("Here are the toppings:")
    for topping in toppings:
        print(f"\t{topping}")


make_pizza2(12, 'mushrooms', 'cheese')
