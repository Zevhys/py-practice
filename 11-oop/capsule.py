"""
! category: easy
TODO: 1. Create a Student class with the following attributes: __name (private): student name, __nim (private): student ID number, __score (private): student's score (0-100). 2. Implement the following methods in the Student class: Constructor to initialize attributes, Getters and setters for the name and nim attributes, Setter for score that ensures the value is not less than 0 and not more than 100, Method get_grade() that returns a grade based on the score: A: 80-100, B: 70-79, C: 60-69, D: 50-59, E: 0-49.
"""


class Student:
    def __init__(self, name, nim, score=0):
        self.__name = name
        self.__nim = nim
        self.set_score(score)

    def get_name(self):
        return self.__name

    def set_name(self, name):
        self.__name = name

    def get_nim(self):
        return self.__nim

    def set_nim(self, nim):
        self.__nim = nim

    def set_score(self, score):
        if 0 <= score <= 100:
            self.__score = score
            return True
        else:
            if not hasattr(self, "_Student__score"):
                self.__score = 0
            print("Value must be between 0 and 100")
            return False

    def get_score(self):
        return self.__score

    def get_grade(self):
        if self.__score >= 80:
            return "A"
        elif self.__score >= 70:
            return "B"
        elif self.__score >= 60:
            return "C"
        elif self.__score >= 50:
            return "D"
        else:
            return "E"


student1 = Student("Budi", "12345", 85)
print(f"name: {student1.get_name()}")
print(f"nim: {student1.get_nim()}")
print(f"score: {student1.get_score()}")
print(f"Grade: {student1.get_grade()}\n")

student1.set_name("rayleigh")
student1.set_nim("001")
student1.set_score(70)
print(f"new name: {student1.get_name()}")
print(f"new nim: {student1.get_nim()}")
print(f"new score: {student1.get_score()}")
print(f"new grade: {student1.get_grade()}\n")

student1.set_score(-10)
print(f"after: {student1.get_score()}\n")

"""
! category: medium
TODO: 1. Create a MediaFile class with the following attributes: __title (private): file title, __artist (private): artist name, __duration (private): duration in seconds, __played_count (private): how many times the media has been played. 2. Implement the following methods in the MediaFile class: Constructor to initialize attributes, Getters for all attributes, Method play() that increases __played_count and displays the message "Playing [title] by [artist]", Method get_duration_str() that converts duration from seconds to "mm:ss" format. 3. Create a MediaPlayer class that will use abstraction to hide media management details: Attribute __playlist (private): list to store MediaFile objects, Methods: add_media(title, artist, duration): creates a new MediaFile object and adds it to the playlist, play_media(title): plays media with a specific title, get_most_played(): returns the most frequently played media, display_playlist(): displays all media in the playlist.
"""


class MediaFile:
    def __init__(self, title, artist, duration=0, played_count=0):
        self.__title = title
        self.__artist = artist
        self.__duration = duration
        self.__played_count = played_count

        def get_title(self):
            return self.__title

        def get_artist(self):
            return self.__artist

        def get_duration(self):
            return self.__duration

        def get_played_count(self):
            return self.__played_count

        def play(self):
            self.__played_count += 1
            print("")
            print(f"playing {self.__title} by {self.__artist}")

        def get_duration_str(self):
            minute = self.__duration // 60
            second = self.__duration % 60

            return f"{minute:02d}:{second:02d}"


class MediaPlayer:
    def __init__(self):
        self.__playlist = []

    def add_media(self, title, artist, duration):
        new_media = MediaFile(title, artist, duration)
        self.__playlist.append(new_media)
        print(f"added: {title} by {artist}")

    def play_media(self, title):
        for media in self.__playlist:
            if media.get_title().lower() == title.lower():
                media.play()
                return True
        print(f"media '{title}' not found in playlist")
        return False

    def get_most_played(self):
        if not self.__playlist:
            print("playlist is empty")
            return None

        most_played = self.__playlist[0]
        for media in self.__playlist[1:]:
            if media.get_played_count() > most_played.get_played_count():
                most_played = media

        return most_played

    def display_playlist(self):
        if not self.__playlist:
            print("playlist is empty")
            return

        print("\n=== PLAYLIST ===")
        for i, media in enumerate(self.__playlist, 1):
            title = media.get_title()
            artist = media.get_artist()
            duration = media.get_duration_str()
            play_count = media.get_played_count()
            print(f"{i}. {title} by {artist} ({duration}) - played {play_count} times")


if __name__ == "__main__":
    player = MediaPlayer()

    player.add_media("Shape of You", "Ed Sheeran", 235)
    player.add_media("Blinding Lights", "The Weeknd", 200)
    player.add_media("Dance Monkey", "Tones and I", 210)

    player.display_playlist()

    player.play_media("Shape of You")
    player.play_media("Blinding Lights")
    player.play_media("Blinding Lights")
    player.play_media("Dance Monkey")

    player.display_playlist()

    most_played = player.get_most_played()
    if most_played:
        print(
            f"\nmost played: {most_played.get_title()} by {most_played.get_artist()} - played {most_played.get_played_count()} times"
        )
