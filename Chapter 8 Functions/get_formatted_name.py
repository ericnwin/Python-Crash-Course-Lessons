def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        full_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        full_name = f"{first_name.title()} {last_name.title()}"
    return full_name


print(get_formatted_name('eric', 'nguyen'))

print(get_formatted_name('miles', 'davis', 'trevino'))
