'''
9-15. Lottery Analysis: You can use a loop to see how hard it might be to win
the kind of lottery you just modeled. Make a list or tuple called my_ticket .
Write a loop that keeps pulling numbers until your ticket wins. Print a message
reporting how many times the loop had to run to give you a winning ticket.
'''
import random
import string


def generate_ticket(number_characters=4):
    ticket = []
    letters = string.ascii_lowercase
    list_letters = ''.join(random.choice(letters)
                           for i in range(number_characters+1))
    # returns a random list of 5 letters

    list_numbers = [random.randint(1, 10) for i in range(10)]
    # return a random list of 10 letters
    list_numbers.extend(list_letters)  # adding list 1 and list 2 together
    #   random.shuffle(list_numbers)
    #ticket = random.choices(list_numbers, k=number_characters)
    while len(ticket) < 4:
        character = random.choice(list_numbers)
        if character not in ticket:
            ticket.append(character)

    return ticket

    # choice returns rand single element from list tuple etc
    # choices returns rand element with k sized list


def compare_ticket(winning_ticket, ticket):
    for ticket_c in ticket:
        if ticket_c not in winning_ticket:
            return False
    return True


winning_ticket = generate_ticket()
print(winning_ticket)
won = False

play = 0
max_tries = 1_000_000

while not won:
    play_ticket = generate_ticket()
    play += 1
    won = (compare_ticket(winning_ticket, play_ticket))
    if play > max_tries:
        break
print("Here's the winning ticket: ", winning_ticket)
print("Here's your ticket: ", play_ticket)
print("Here's the number of tries: ", play)
