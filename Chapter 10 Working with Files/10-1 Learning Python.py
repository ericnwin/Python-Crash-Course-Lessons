'''
10-1. Learning Python: Open a blank file in your text editor and write a few
lines summarizing what you’ve learned about Python so far. Start each line
with the phrase In Python you can. . . . Save the file as learning_python.txt in
the same directory as your exercises from this chapter. Write a program that
reads the file and prints what you wrote three times. Print the contents once by
reading in the entire file, once by looping over the file object, and once by stor-
ing the lines in a list and then working with them outside the with block.
'''
# Reading over entire file
file_path = '/home/ericnguyen/Python/Python Crash Course/Chapter 10 Working with Files/learning_python.txt'
with open(file_path) as file_object:
    print("---Reading over entire file")
    content = file_object.read()
    print(content)

# Looping over the file object
print("\n---Looping over the file object")
with open(file_path) as file_object:
    for line in file_object:
        print(line.rstrip())

# Storing lines in a list and accessing it outside of with block

print("\n---Storing lines in a list")
with open(file_path) as file_object:
    lines = file_object.readlines()

for line in lines:
    print(line.rstrip())


with open(file_path) as file_object:
    content = file_object.readlines()
print("\n---Replacing another language")
for line in content:
    a = line.replace("Python", "C")
    print(a.rstrip())
