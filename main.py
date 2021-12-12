import lyricsgenius
import sys
genius = lyricsgenius.Genius("UaPyhGcLZMQKo-EMCzpATT0s3N_MTp4Dl9gQ-KjfFzY7e54_--VcS7fGli9vA6cq")
input_artist = sys.argv[1]
artist = genius.search_artist(input_artist, max_songs = 3)
print(artist.songs)
artist.save_lyrics()

