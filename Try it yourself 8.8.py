def make_album(artist_name, album_title, num_tracks=None):

    album = {
        'artist': artist_name,
        'title': album_title,
    }
    if num_tracks is not None:
        album['tracks'] = num_tracks
    return album

print("Enter 'q' at any time to quit.\n")

while True:
    artist = input("Enter the artist's name: ")
    if artist.lower() == 'q':
        break
        
    title = input("Enter the album title: ")
    if title.lower() == 'q':
        break
        
    album_info = make_album(artist, title)
    print("\nCreated Album Dictionary:")
    print(album_info)
