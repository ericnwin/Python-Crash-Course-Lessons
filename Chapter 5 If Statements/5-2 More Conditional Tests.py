'''
5-2. More Conditional Tests: You don’t have to limit the number of tests you
create to ten. If you want to try more comparisons, write more tests and add
them to conditional_tests.py. Have at least one True and one False result for
each of the following:
• Tests for equality and inequality with strings
• Tests using the lower() method
• Numerical tests involving equality and inequality, greater than and
less than, greater than or equal to, and less than or equal to
• Tests using the and keyword and the or keyword
• Test whether an item is in a list
• Test whether an item is not in a list
'''

disney_character = "mickey mouse"
print('goofy' == disney_character)
print('donald duck' != disney_character)

fruit = 'Clementine'
print(fruit.lower() == 'banana')
print(fruit.lower() == 'clementine')

print("\n Here are the numerical comparisons:")
print(9 > 21)
print(9 >= 21)
print(9 < 21)
print(9 <= 21)

human_body = 'vagina'
human_body2 = 'ovaries'
if human_body == 'penis' and human_body2 == 'balls':
    print("its a boy!")
else:
    print("it's a girl!")


speed_limit = 40
driver_speed = 40
legal_alcohol_content = .0008
driver_alcohol_content = .0005
if (driver_speed > speed_limit) or (legal_alcohol_content <= driver_alcohol_content):
    print("\nWEE WHOO WEE WHOO. Stop right there and put your hands behind your back")
else:
    print("\nYou're free to go, sorry for the trouble")


fav_parks = ['disneyland', 'six flags',
             'hurricane harbor', 'california adventure park']
print('SIX FLAGS   '.strip().lower() in fav_parks)
