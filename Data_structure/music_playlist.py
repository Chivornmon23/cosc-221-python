class Node:
    def __init__(self, song_name):
        self.song_name = song_name
        self.next = None

class Playlist:
    def __init__(self):
        self.head = None

    def add_song(self, song_name):
        new_song = Node(song_name)
        if not self.head:
            self.head = new_song
        else:
            current_song = self.head
            while current_song.next:
                current_song = current_song.next
            current_song.next = new_song

    def play_next(self):
        if not self.head:
            print("No songs in the playlist.")
        else:
            print(f"Now playing: {self.head.song_name}")
            self.head = self.head.next
    def display_songs(self):
        current_song = self.head

        if not current_song:
            print("NO songs in the playlist.")
        else:
            while current_song:
                print(current_song.song_name)
                current_song = current_song.next

playlist = Playlist()
playlist.add_song("One Wish")
playlist.add_song("Sure thing!")
playlist.add_song("If I aint got you.")
playlist.add_song("You by young Lloyd")

print("All songs:")
playlist.display_songs()

print("\nPlaying next song:")
playlist.play_next()

print("\nRemaining songs:")
playlist.display_songs()