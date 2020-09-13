def get_formatted_name(first_name, last_name, middle_name=''):
    if middle_name:
        formatted_name = f"{first_name.title()} {middle_name.title()} {last_name.title()}"
    else:
        formatted_name = f"{first_name.title()} {last_name.title()}"
    print(formatted_name)
    return formatted_name
