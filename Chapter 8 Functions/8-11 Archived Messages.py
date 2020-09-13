'''
8-11. Archived Messages: Start with your work from Exercise 8-10. Call the
function send_messages() with a copy of the list of messages. After calling the
function, print both of your lists to show that the original list has retained its
messages.
'''


def send_messages(message, sent_messages):
    while message:
        current_message = message.pop()
        print(f"Sending: {current_message}\n")
        sent_messages.append(current_message)
    for text in sent_messages:
        print(f"Sent: {text}\n")


texts = ['i <3 you', 'haha noob xD', 'aghh promise?']
sent_texts = []

send_messages(texts[:], sent_texts)
print(texts)
