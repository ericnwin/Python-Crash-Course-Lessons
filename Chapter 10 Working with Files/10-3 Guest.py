'''
10-3. Guest: Write a program that prompts the user for their name. When they
respond, write their name to a file called guest.txt.
'''
file_path = '/home/ericnguyen/Python/Python Crash Course/Chapter 10 Working with Files/guest.txt'

with open(file_path, 'w') as file_object:
    file_object.write(input("whats your name?"))
    print("okay got it! Cool name btw")


'''
10-4. Guest Book: Write a while loop that prompts users for their name. When
they enter their name, print a greeting to the screen and add a line recording
their visit in a file called guest_book.txt. Make sure each entry appears on a
new line in the file.
'''

file_path2 = '/home/ericnguyen/Python/Python Crash Course/Chapter 10 Working with Files/guest_book.txt'

with open(file_path2, 'a') as file_object:
    while True:
        name = input(
            "Thank you for staying. whats your name?\nEnter 'Q' if you want to leave: ")
        file_object.write(f"{name} \n")
        print("Hello ", name, '\n')
        if name == 'q':
            break
