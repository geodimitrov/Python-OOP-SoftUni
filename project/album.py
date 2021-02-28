from song import Song

class Album:
    def __init__(self, name, songs):
        self.name = name
        self.songs = songs
        self.published = False

    def add_song(self, song):

        return f"Song {song.name} has been added to the album {self.name}."

    def remove_song(self, song_name: str):
        pass

    def publish(self):
        pass

    def details(self):
        pass

# Test Code

song = Song("Running in the 90s", 3.45, False)
print(song.get_info())
album = Album("Initial D", song)
second_song = Song("Around the World", 2.34, False)
print(album.add_song(second_song))
print(album.details())
print(album.publish())