'''
8-9. Messages: Make a list containing a series of short text messages. Pass the
list to a function called show_messages() , which prints each text message.
'''


def show_messages(texts):
    """
    Will output a series of text messages
    """
    for text in texts:
        print(f"Text: {text}")


text = ['i <3 you', 'b4 you go', 'haha lol']

show_messages(text)
