polling_results = {}

polling_active = True

while polling_active:
    name = input("What's your name?")
    response = input("\tWhat's your favorite game at this moment\n")
    polling_results[name.title()] = response.title()
    adding_person = input("Do you want to add another person? y/n")
    if adding_person == "n":
        polling_active = False

print(polling_results)
