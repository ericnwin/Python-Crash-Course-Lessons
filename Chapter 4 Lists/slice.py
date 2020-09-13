# Getting specific index ranges in a list SIMILAR TO MATLAB

players = ['thijs', 'messi', 'kobe', 'faker', 'shroud']
print(players[2:])


# Can use a for loop to display specific info by using slices
print("Here are my 2 best players:")
for top in players[3:]:
    print(top.title())


# To copy a list just use [:]

list1 = ['a', 'b', 'c']
list2 = list1[:]
list1.append("d")
list2.append("e")
print(list1)
print(list2)
