'''
8-13. User Profile: Start with a copy of user_profile.py from page 149. Build a
profile of yourself by calling build_profile() , using your first and last names
and three other key-value pairs that describe you.

def function(**parameter) will create a dictionary
called parameter
TO ADD TO **parameter:
    function(location='london', education='bachelors')
'''


def user_profile(first, last, **user_info):
    user_info['first name'] = first
    user_info['last name'] = last
    return user_info


student_eric = user_profile('eric', 'nguyen', occupation='student',
                            major='electrical engineering')
print(student_eric)
