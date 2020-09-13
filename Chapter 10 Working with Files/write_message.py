'''
Using programming.txt write a message inside
NOTE: using open(file_path,'w') will erase and write in your new contents
'''
file_path = '/home/ericnguyen/Python/Python Crash Course/Chapter 10 Working with Files/programming.txt'
with open(file_path, 'a') as file_object:
    file_object.write("I love Python\n")
    file_object.write(str(69))
    file_object.write("\nI just wrote a new line")
