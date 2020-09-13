# You just found out that your new dinner table won’t
# arrive in time for the dinner, and you have space for only two guests.
# • Start with your program from Exercise 3-6. Add a new line that prints a
# message saying that you can invite only two people for dinner.
# • Use pop() to remove guests from your list one at a time until only two
# names remain in your list. Each time you pop a name from your list, print
# a message to that person letting them know you’re sorry you can’t invite
# them to dinner.
# • Print a message to each of the two people still on your list, letting them
# know they’re still invited.
# • Use del to remove the last two names from your list, so you have an empty
# list. Print your list to make sure you actually have an empty list at the end
# of your program.

dinner_guests = ['Joeji', 'Elon Musk', 'OpenAI']

print(
    f"Hey {dinner_guests[0]} I'm a huge fan of your music! Please join me for dinner. ")
print(f"Hey {dinner_guests[1]} can I get a free car? We can talk over dinner.")
print(f"Hey {dinner_guests[2]} teach me AI. I gib food as payment.")

# Declare who can't make it
declined_invitations = "OpenAI"
dinner_guests.remove(declined_invitations)
print(f"Unfortunately {declined_invitations} can't make it.\n")

# Adding new person to invite list
new_person_invite = "Kanye West"
dinner_guests.append(new_person_invite)
print(dinner_guests)

# Making 2nd set of invitations
print(
    '\n' f"Hey {dinner_guests[0]} I'm a huge fan of your music! Please join me for dinner. ")
print(f"Hey {dinner_guests[1]} can I get a free car? We can talk over dinner.")
print(f"Hey {dinner_guests[2]} I loved you in Titanic. Please eat with me.\n")

# shrinking down to 2 people and sending msg to those who are invited
print(f"Hey sorry  we only have room for two... I'm uninviting one of you sorry.\n")

uninvited = dinner_guests.pop()
print(f"Hey sorry {uninvited} you've been uninvited :( \n")

print(f"Hey {dinner_guests[0]} you're still invited.")
print(f"Hey {dinner_guests[1]} you're still invited.")

# Remove last 2 names from list and printing out an empty list
del dinner_guests[0]
del dinner_guests[0]


print(dinner_guests)
