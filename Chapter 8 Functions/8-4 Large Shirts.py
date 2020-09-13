'''
8-4. Large Shirts: Modify the make_shirt() function so that shirts are large
by default with a message that reads I love Python. Make a large shirt and a
medium shirt with the default message, and a shirt of any size with a different
message.
'''


def make_shirt(size='large', text='I love Python'):
    print(f"I'll be making a {size.title()} shirt! \n")
    print(f"Here's the text :\n\t{text}\n")


make_shirt('medium', "I'm with stupid -->")

make_shirt(size='large', text="BLM")

make_shirt()

make_shirt('medium')
make_shirt(size='small', text='i like big booties')
