'''
8-10. Sending Messages: Start with a copy of your program from Exercise 8-9.
Write a function called send_messages() that prints each text message and
moves each message to a new list called sent_messages as it’s printed. After
calling the function, print both of your lists to make sure the messages were
moved correctly.
'''


def send_messages(texts, sent_texts):
    """
    Will output a series of text messages
    """
    while texts:
        current_text = texts.pop()
        print(f"Printing this text: {current_text}\n")
        sent_texts.append(current_text)
    for text in sent_texts:
        print(f"Here's the sent texts: {text}\n")


texts = ['i <3 you', 'haha noob xD', 'aghh promise?']
sent_texts = []

send_messages(texts, sent_texts)
