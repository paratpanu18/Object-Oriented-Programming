# 66010542

from abc import ABC, abstractmethod, abstractproperty

class AudioFile(ABC):
    def __init__(self, media_name):
        self.__media_name = media_name

    @property
    def media_name(self):
        return self.__media_name

    @abstractmethod
    def play(self):
        pass

class Mp3File(AudioFile):
    def play(self):
        return f'Playing MP3 File: {self.media_name}'

class FlacFile(AudioFile):
    def play(self):
        return f'Playing FLAC File: {self.media_name}'

class AccFile(AudioFile):
    def play(self):
        return f'Playing ACC File: {self.media_name}'

class PodcastEpisode():
    def __init__(self, episode_no, episode_file):
        self.__episode_no = episode_no
        self.__episode_file = episode_file

    @property
    def episode_name(self):
        return self.__episode_file.media_name

    def play(self):
        return self.__episode_file.play() 


class PodcastChanel():
    def __init__(self, host_name, chanel_name):
        self.__host_name = host_name
        self.__chanel_name = chanel_name
        self.__episode_list = []

    @property
    def chanel_name(self):
        return self.__chanel_name

    def add_episode_to_podcast_chanel(self, episode_no, episode_file):
        new_episode = PodcastEpisode(episode_no, episode_file)
        self.__episode_list.append(new_episode)

    def get_episode_by_episode_name(self, episode_name):
        for episode in self.__episode_list:
            if episode.episode_name == episode_name:
                return episode
        return None


class Music():
    def __init__(self, song_file):
        self.__song_file = song_file

    @property
    def song_name(self):
        return self.__song_file.media_name

    def play(self):
        return self.__song_file.play()

class Artist():
    def __init__(self, artist_name):
        self.__artist_name = artist_name
        self.__album_list = []

    @property
    def artist_name(self):
        return self.__artist_name

    @property
    def album_list(self):
        return self.__album_list

    def add_album_to_artist(self, new_album):
        if isinstance(new_album, Album):
            # Check if New Album is already exist
            if self.album_is_exist(new_album):
                raise ValueError(f'This album ({new_album.album_name}) is already existed')

            self.__album_list.append(new_album)

        else:
            raise ValueError("Not an Album")

    def get_album_by_album_name(self, album_name):
        for album in self.__album_list:
            if album.album_name == album_name:
                return album
        return None

    def album_is_exist(self, new_album):
        for existing_album in self.__album_list:
            if existing_album.album_name == new_album.album_name:
                return True
            return False

class  Album():
    def __init__(self, album_name):
        self.__album_name = album_name
        self.__song_list = []

    @property
    def album_name(self):
        return self.__album_name

    def add_song_to_album(self, new_song):
        if isinstance(new_song, Music):

            if self.song_is_exist(new_song):
                raise ValueError(f'This song ({new_song.song_name}) is already existed.')

            self.__song_list.append(new_song)
        else:
            raise ValueError("Not a song")

    def get_song_by_song_name(self, song_name):
        for song in self.__song_list:
            if song.song_name == song_name:
                return song
        return None

    def song_is_exist(self, new_song):
        for existing_song in self.__song_list:
            if existing_song.song_name == new_song.song_name:
                return True
        return False

    def play(self):
        for song in self.__song_list:
            print(song.play())

class Playlist():
    def __init__(self, playlist_name):
        self.__playlist_name = playlist_name
        self.__media_list = []

    @property
    def playlist_name(self):
        return self.__playlist_name

    def add_media_to_playlist(self, new_media):
        self.__media_list.append(new_media)

    def play(self):
        for media in self.__media_list:
            print(media.play())

class MediaPlayer:
    def __init__(self):
        self.__artists_list = []
        self.__podcast_channel_list = []
        self.__playlist = []

    def play_song(self, album_name, artist_name, song_name):
        artist = self.get_artist_by_artist_name(artist_name)
        if not artist:
            raise ValueError("Artist not found")

        album = artist.get_album_by_album_name(album_name)
        if not album:
            raise ValueError("Album not found.")

        song = album.get_song_by_song_name(song_name)
        if not song:
            raise ValueError("Music not found.")

        print(song.play())

    def play_podcast(self, episode_name, chanel_name):
        podcast_chanel = self.get_podcast_chanel_by_name(chanel_name)
        if not podcast_chanel:
            raise ValueError("Podcast Chanel not found.")

        episode = podcast_chanel.get_episode_by_episode_name(episode_name)
        if not episode:
            raise ValueError("Episode not found.")

        print(episode.play())

    def play_playlist(self, playlist_name):
        playlist = self.get_playlist_by_name(playlist_name)
        if not playlist:
            raise ValueError("Playlist not found.")

        playlist.play()

    def play_album(self, album_name, artist_name):
        artist = self.get_artist_by_artist_name(artist_name)
        if not artist:
            raise ValueError("Artist not found")

        album = artist.get_album_by_album_name(album_name)
        if not album:
            raise ValueError("Album not found.")

        album.play()

    def get_artist_by_artist_name(self, artist_name):
        for artist in self.__artists_list:
            if artist.artist_name == artist_name:
                return artist
        return None

    def get_podcast_chanel_by_name(self, chanel_name):
        for podcast_chanel in self.__podcast_channel_list:
            if podcast_chanel.chanel_name == chanel_name:
                return podcast_chanel
        return None

    def add_artist(self, artist_name):
        new_artist = Artist(artist_name)
        self.__artists_list.append(new_artist)

    def add_album(self, artist_name, album_name):
        artist = self.get_artist_by_artist_name(artist_name)
        if not artist:
            raise ValueError("Artist not found")

        artist.add_album_to_artist(Album(album_name))

    def add_song_to_album(self, artist_name, album_name, song_file):
        artist = self.get_artist_by_artist_name(artist_name)
        if not artist:
            raise ValueError("Artist not found")

        album = artist.get_album_by_album_name(album_name)
        if not album:
            raise ValueError("Album not found.")

        album.add_song_to_album(Music(song_file))

    def add_podcast_chanel(self, host_name, chanel_name):
        new_podcast_chanel = PodcastChanel(host_name, chanel_name)
        self.__podcast_channel_list.append(new_podcast_chanel)

    def add_episode_to_podcast_chanel(self, chanel_name, episode_no, episode_file):
        podcast_chanel = self.get_podcast_chanel_by_name(chanel_name)
        if not podcast_chanel:
            raise ValueError("Chanel not found.")

        podcast_chanel.add_episode_to_podcast_chanel(episode_no, episode_file)

    def add_playlist(self, playlist_name):
        new_playlist = Playlist(playlist_name)
        self.__playlist.append(new_playlist)

    def get_playlist_by_name(self, playlist_name):
        for playlist in self.__playlist:
            if playlist.playlist_name == playlist_name:
                return playlist
        return None

    def add_song_to_playlist(self, artist_name, album_name, song_name, playlist_name):
        playlist = self.get_playlist_by_name(playlist_name)
        if not playlist:
            raise ValueError("Playlist not found.")

        artist = self.get_artist_by_artist_name(artist_name)
        if not artist:
            raise ValueError("Artist not found")

        album = artist.get_album_by_album_name(album_name)
        if not album:
            raise ValueError("Album not found.")

        song = album.get_song_by_song_name(song_name)
        if not song:
            raise ValueError("Music not found.")

        playlist.add_media_to_playlist(song)

    def add_podcast_episode_to_playlist(self, chanel_name, episode_name, playlist_name):
        playlist = self.get_playlist_by_name(playlist_name)
        if not playlist:
            raise ValueError("Playlist not found.")

        podcast_chanel = self.get_podcast_chanel_by_name(chanel_name)
        if not podcast_chanel:
            raise ValueError("Podcast Chanel not found.")

        episode = podcast_chanel.get_episode_by_episode_name(episode_name)
        if not episode:
            raise ValueError("Episode not found.")

        playlist.add_media_to_playlist(episode)

    def search_song(self, song_name):
        for artist in self.__artists_list:
            # In case that song_name is album_name; play entire album
            album = artist.get_album_by_album_name(song_name)
            if album:
                album.play()
                return

            for album in artist.album_list:
                song = album.get_song_by_song_name(song_name)
                if song:
                    print(song.play())
                    return

player = MediaPlayer()

player.add_artist(artist_name="Ed Sheeran")         # Add artist named Ed Sheeran

# Add 2 album
player.add_album(artist_name="Ed Sheeran", album_name="Shape of You")
player.add_album(artist_name="Ed Sheeran", album_name="=")

# Add song to album
player.add_song_to_album(artist_name="Ed Sheeran", album_name="Shape of You", song_file=Mp3File("Shape of You"))
player.add_song_to_album(artist_name="Ed Sheeran", album_name="Shape of You", song_file=Mp3File("Shape of You - Acoustic"))

player.add_song_to_album(artist_name="Ed Sheeran", album_name="=", song_file=Mp3File("Bad Habits"))
player.add_song_to_album(artist_name="Ed Sheeran", album_name="=", song_file=FlacFile("Shivers"))

# Add PodcastChanel
player.add_podcast_chanel(host_name="Lex Fridman", chanel_name="Lex Fridman Podcast")
player.add_episode_to_podcast_chanel(chanel_name="Lex Fridman Podcast", episode_no=1, episode_file=AccFile("Yann Lecun"))
player.add_episode_to_podcast_chanel(chanel_name="Lex Fridman Podcast", episode_no=1, episode_file=Mp3File("Elon Musk"))

# Create playlist
player.add_playlist(playlist_name="1")

# Add media to playlist
player.add_song_to_playlist(artist_name="Ed Sheeran", album_name="=", song_name="Bad Habits", playlist_name="1")
player.add_podcast_episode_to_playlist(chanel_name="Lex Fridman Podcast", episode_name="Yann Lecun", playlist_name="1")
player.add_podcast_episode_to_playlist(chanel_name="Lex Fridman Podcast", episode_name="Elon Musk", playlist_name="1")      # เพิ่่มตาม  Test Case

# Testcase 1 : เล่นเพลง โดยส่ง instance ของเพลง และ instance ของ podcast
# Expected output 
# Playing MP3 file :  Shape of You
# Playing aac file :  Yann Lecun
print("Testcase 1 : เล่นเพลง โดยส่ง instance ของเพลง และ instance ของ podcast")
player.play_song("Shape of You","Ed Sheeran","Shape of You")
player.play_podcast(episode_name="Yann Lecun", chanel_name="Lex Fridman Podcast")
print()

# Testcase 2 : เล่นเพลงใน Playlist โดยแสดงชื่อของ media ใน playlist ตามลำดับ
# Expected output
# Playing MP3 file :  Bad Habits
# Playing MP3 file :  Elon Musk

# ! โจทย์กับ Testcase ไม่เหมือนกัน จึงเพิ่ม Podcast episode "Elon Musk" ลงไปใน Playlist "1"
print("Testcase 2 : เล่นเพลงใน Playlist โดยแสดงชื่อของ media ใน playlist ตามลำดับ")
player.play_playlist("1")
print()

# Testcase 3 : เล่นเพลงใน Album โดยแสดงชื่อของ media ใน Album ตามลำดับ
# Expected output
# Playing MP3 file :  Shape of You
# Playing MP3 file :  Shape of You - Acoustic
print("Testcase 3 : เล่นเพลงใน Album โดยแสดงชื่อของ media ใน Album ตามลำดับ")
player.play_album("Shape of You", "Ed Sheeran")
print()

# Testcase 4 : ค้นหาเพลง
# Expected output
# Playing MP3 file :  Bad Habits
# Playing MP3 file :  Shape of You
# Playing MP3 file :  Shape of You - Acoustic
print("Testcase 4 : ค้นหาเพลง")
player.search_song("Bad Habits")
player.search_song("Shape of You")
