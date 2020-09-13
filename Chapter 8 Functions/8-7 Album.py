'''
8-7. Album: Write a function called make_album() that builds a dictionary
describing a music album. The function should take in an artist name and an
album title, and it should return a dictionary containing these two pieces of
information. Use the function to make three dictionaries representing different
albums. Print each return value to show that the dictionaries are storing the
album information correctly.
Use None to add an optional parameter to make_album() that allows you to
store the number of songs on an album. If the calling line includes a value for
the number of songs, add that value to the album’s dictionary. Make at least
one new function call that includes the number of songs on an album.
'''


def make_album(artist_name, album_title, songs=None):
    if songs:
        return {'artist name': artist_name, 'album title': album_title, 'number of songs': songs}
    return {'artist name': artist_name, 'album title': album_title}


print(make_album('Joji', 'Ballads 1'))

print(make_album('Yeek', 'Cleaner Air'))

print(make_album('Tyler the Creator', 'Flower Boy'))

print(make_album('Umi', 'Butterfly', 1))
