'''
7-5. Movie Tickets: A movie theater charges different ticket prices depending on
a person’s age. If a person is under the age of 3, the ticket is free; if they are
between 3 and 12, the ticket is $10; and if they are over age 12, the ticket is
$15. Write a loop in which you ask users their age, and then tell them the cost
of their movie ticket.
'''

prompt = "What's your age?"

age = input(prompt)
age = int(age)
while True:
    if age < 3:
        ticket = 0
    elif 3 <= age <= 12:
        ticket = 10
    else:
        ticket = 15
    print(f"Your movie tickets costs ${ticket}")
    break
