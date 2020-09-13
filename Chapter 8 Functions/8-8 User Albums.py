'''
8-8. User Albums: Start with your program from Exercise 8-7. Write a while
loop that allows users to enter an album’s artist and title. Once you have that
information, call make_album() with the user’s input and print the dictionary
that’s created. Be sure to include a quit value in the while loop.
'''


def make_album(artist_name, album_title, songs=None):
    if songs:
        return {'artist name': artist_name, 'album title': album_title, 'number of songs': songs}
    return {'artist name': artist_name, 'album title': album_title}


while True:
    print("(You can enter 'q' if you want to leave.)")
    a_name = input("What's your performing name?")
    if a_name == 'q':
        break
    album_t = input("What's your album title's name?")
    if album_t == 'q':
        break
    song_number = input("How many songs are on the album?")
    if song_number == 'q':
        break
    print(make_album(a_name, album_t, song_number))
