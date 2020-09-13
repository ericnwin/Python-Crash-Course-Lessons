'''
Using functions to take in a list as input (unprinted_model) then outputting it to
another list (completed_model)
'''

unprinted_model = ['fidget spinner', 'record', 'topo map of LA']
completed_model = []


def print_models(unprinted_model, completed_model):
    """
    Simulate printing each design until none are left. Moves it to
    another list completed_models after printing.
    """
    while unprinted_model:
        current_design = unprinted_model.pop()
        print(f"Making this currently: {current_design}")
        completed_model.append(current_design)


def show_completed_models(completed_model):
    """
    Output the list completed model as a single entry
    """
    for model in completed_model:
        print(f"I finished making: {model}")


#print_models(unprinted_model, completed_model)
# show_completed_models(completed_model)


# If we want to leave list unprinted_model intact, we can just copy the list w/
# print_models(unprinted_model[:],completed_model)

print_models(unprinted_model[:], completed_model)
show_completed_models(completed_model)
print(unprinted_model)
