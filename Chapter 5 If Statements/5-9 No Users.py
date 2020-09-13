'''
5-9. No Users: Add an if test to hello_admin.py to make sure the list of users is
not empty.
• If the list is empty, print the message We need to find some users!
• Remove all of the usernames from your list, and make sure the correct
message is printed.
'''
usernames = []
#usernames = ['admin', 'bigbooty69', 'analbeads', 'digbick', 'cum420']
if usernames:
    for username in usernames:
        if username == 'admin':
            print('Hello admin, would you like to see a status report on your server?')
        else:
            print(f'Greetings, {username} enjoy your stay on our server!')
else:
    print("you need to add some users!")
