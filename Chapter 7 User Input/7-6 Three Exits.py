'''
7-6. Three Exits: Write different versions of either Exercise 7-4 or Exercise 7-5
that do each of the following at least once:
• Use a conditional test in the while statement to stop the loop.
• Use an active variable to control how long the loop runs.
• Use a break statement to exit the loop when the user enters a 'quit' value.
'''
prompt = "What's your age?"
prompt += "\nEnter 'quit' if you wanna leave: "
age = input(prompt)
#age = int(age)
'''
while True:
   if age == 'quit':
        break
    elif age < 3:
        ticket = 0
    elif 3 <= age <= 12:
        ticket = 10
    else:
        ticket = 15
    print(f"Your movie tickets costs ${ticket}")
    break
'''

while age != 'quit':
    age = int(age)
    if age < 3:
        ticket = 0
    elif 3 <= age <= 12:
        ticket = 10
    else:
        ticket = 15
    print(f"Your movie tickets costs ${ticket}")
    break
