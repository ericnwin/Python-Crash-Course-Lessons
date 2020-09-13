'''
import os
this_dir = os.path.dirname(os.path.abspath(__file__))
print(this_dir)
'''
file_path = '/home/ericnguyen/Python/Python Crash Course/Chapter 10 Working with Files/pi.txt'

with open(file_path) as file_object:
    lines = file_object.readlines()

pi_string = ''
for line in lines:
    pi_string += line.rstrip()

print(pi_string)
