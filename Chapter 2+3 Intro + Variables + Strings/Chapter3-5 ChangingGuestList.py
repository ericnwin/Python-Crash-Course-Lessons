# You just heard that one of your guests can’t make the
# dinner, so you need to send out a new set of invitations. You’ll have to think of
# someone else to invite.
# 
# • Start with your program from Exercise 3-4. Add a print() call at the end
# of your program stating the name of the guest who can’t make it.
# 
# • Modify your list, replacing the name of the guest who can’t make it with
# the name of the new person you are inviting.
# 
# • Print a second set of invitation messages, one for each person who is still
# in your list.

dinner_guests = ['Joeji', 'Elon Musk', 'OpenAI']

print (f"Hey {dinner_guests[0]} I'm a huge fan of your music! Please join me for dinner. ")
print (f"Hey {dinner_guests[1]} can I get a free car? We can talk over dinner.")
print (f"Hey {dinner_guests[2]} teach me AI. I gib food as payment.")

#Declare who can't make it
declined_invitations = "OpenAI"
dinner_guests.remove(declined_invitations)
print(f"Unfortunately {declined_invitations} can't make it.")

#Adding new person to invite list
new_person_invite = "Kanye West"
dinner_guests.append(new_person_invite)
print(dinner_guests)

#Making 2nd set of invitations
print (f"Hey {dinner_guests[0]} I'm a huge fan of your music! Please join me for dinner. ")
print (f"Hey {dinner_guests[1]} can I get a free car? We can talk over dinner.")
print (f"Hey {dinner_guests[2]} I loved you in Titanic. Please eat with me.")