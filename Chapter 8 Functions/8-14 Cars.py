'''
8-14. Cars: Write a function that stores information about a car in a diction-
ary. The function should always receive a manufacturer and a model name. It
should then accept an arbitrary number of keyword arguments. Call the func-
tion with the required information and two other name-value pairs, such as a
color or an optional feature. Your function should work for a call like this one:
car = make_car('subaru', 'outback', color='blue', tow_package=True)
Print the dictionary that’s returned to make sure all the information was
stored correctly.
'''


def car_info(manufacturer, model, **karg):
    karg['manufacturer'] = manufacturer
    karg['model'] = model
    return karg


car = car_info('honda', 'civic', color='silver', trim='sport')
print(car)


# make sure to return the **parameter (in this case **karg) as thats what
# you wanna output the function itself just creates the dictionary