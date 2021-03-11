
class Album:
    def __init__(self, name, *songs):
        self.name = name
        self.songs = list(songs)
        self.published = False

    def add_song(self, song):
        if song.single:
            return f"Cannot add {song.name}. It's a single"
        if self.published:
            return "Cannot add songs. Album is published."
        if song not in self.songs:
            self.songs.append(song)
            return f"Song {song.name} has been added to the album {self.name}."
        return "Song is already in the album."

    def remove_song(self, song_name):
        if self.published:
            return "Cannot remove songs. Album is published."
        song_objs = [song for song in self.songs if song.name == song_name]
        if not song_objs:
            return "Song is not in the album."
        self.songs.remove(song_objs[0])
        return f"Removed song {song_name} from album {self.name}."


    def publish(self):
        if self.published:
            return f"Album {self.name} is already published"
        self.published = True
        return f"Album {self.name} has been published."

    def details(self):
        return f"Album {self.name}\n" + "\n".join(f"== {song.get_info()}" for song in self.songs)


# Test Code
# song = Song("Running in the 90s", 3.45, False)
# print(song.get_info())
# album = Album("Initial D", song)
# second_song = Song("Around the World", 2.34, False)
# print(album.add_song(second_song))
# print(album.details())


