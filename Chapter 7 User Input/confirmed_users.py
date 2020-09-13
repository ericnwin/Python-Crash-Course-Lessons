# Starts with users that need to be verified and an empty list.
# Then move the verified users to a new list confirmed users.

new_users = ['Sally', 'Jennifer', 'Tom']
confirmed_users = []

while new_users:
    verifying_user = new_users.pop()

    print(f"Verifying: {verifying_user.title()}")
    confirmed_users.append(verifying_user)
print(f"Here are the new confirmed users:")
for confirmed_user in confirmed_users:
    print(f"\t{confirmed_user.title()}")


pets = [
    'dog', 'cat', 'snake', 'hamster', 'cat',
    'fish', 'dog', 'cat',
]

print(pets)

while 'cat' in pets:
    pets.remove('cat')


print(pets)
