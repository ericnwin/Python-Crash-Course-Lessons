'''
7-4. Pizza Toppings: Write a loop that prompts the user to enter a series of
pizza toppings until they enter a 'quit' value. As they enter each topping,
print a message saying you’ll add that topping to their pizza.
'''

pizza_toppings = []

prompt = 'What pizza topping would you like?'
prompt += '\nEnter "quit" if you\'re finished: '
while pizza_toppings != 'quit':
    pizza_toppings = input(prompt)
    if pizza_toppings != 'quit':
        print(f"I'll add {pizza_toppings.title()} to your pizza!")
