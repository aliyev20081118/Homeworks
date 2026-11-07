def make_album(artist_name, album_title, num_tracks=None):

    album = {
        'artist': artist_name,
        'title': album_title,
    }
    if num_tracks is not None:
        album['tracks'] = num_tracks
    return album

album1 = make_album('Daft Punk', 'Discovery')
album2 = make_album('Pink Floyd', 'The Dark Side of the Moon')
album3 = make_album('Fleetwood Mac', 'Rumours')

print(album1)
print(album2)
print(album3)

album4 = make_album('Michael Jackson', 'Thriller', num_tracks=9)
print(album4)
