'''
8-3. T-Shirt: Write a function called make_shirt() that accepts a size and the
text of a message that should be printed on the shirt. The function should print
a sentence summarizing the size of the shirt and the message printed on it.
Call the function once using positional arguments to make a shirt. Call the
function a second time using keyword arguments.
'''


def make_shirt(size, text):
    print(f"I'll be making a {size.title()} shirt! \n")
    print(f"Here's the text :\n\t{text}")


make_shirt('medium', "I'm with stupid -->")

make_shirt(size='large', text="BLM")
