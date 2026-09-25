# A linked list is a collection of elements, called nodes, 
#   where each node stores two things:
# 1. Data: The actual value or information.
# 2. Next: A link (or pointer) to the next node in the list

#in simple words, a linked list consists of nodes where each node contains 
# a data field and a reference (link) to the next node in the list.

# L.insertFirst(e): Add element e at the beginning.
# L.insertLast(e): Add element e at the end.
# L.removeFirst(): Remove and return the first element.
# L.removeLast(): Remove and return the last element.
# L.remove(e): Remove the first occurrence of e.
# L.search(e): Return the node with value e, or None if not found.
# L.isEmpty(): Return True if list is empty.
# L.size(): Return the number of nodes in the list.
# L.display(): Print all elements in the list.

# Problem 1:Music Playlist (Linked List)

# Define the Node class for each song in the playlist
class SongNode:
    def __init__(self, song_name):
        self.song_name = song_name  # Name of the song
        self.next = None  # Pointer to the next song

# Define the Playlist class
class Playlist:
    def __init__(self):
        self.head = None  # Start of the playlist
    
    # Add a new song to the playlist
    def add_song(self, song_name):
        new_song = SongNode(song_name)
        if not self.head:  # If the playlist is empty
            self.head = new_song
        else:
            current_song = self.head
            while current_song.next:  # Traverse to the last song
                current_song = current_song.next
            current_song.next = new_song  # Add the new song at the end
    
    # Play the next song in the playlist
    def play_next(self):
        if not self.head:
            print("No songs in the playlist.")
        else:
            print(f"Now playing: {self.head.song_name}")
            self.head = self.head.next  # Move to the next song

# Example usage
playlist = Playlist()

# Add songs to the playlist
playlist.add_song("Song A")
playlist.add_song("Song B")
playlist.add_song("Song C")

# playlist.delete_first()

# Play songs
playlist.play_next()  # Output: Now playing: Song A
playlist.play_next()  # Output: Now playing: Song B
playlist.play_next()  # Output: Now playing: Song C
playlist.play_next()  # Output: No songs in the playlist.
