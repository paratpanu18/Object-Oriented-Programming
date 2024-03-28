from abc import ABC, abstractmethod, abstractproperty

class AudioFile(ABC):
    @abstractmethod
    def play(self):
        pass 

class MP3File(AudioFile):
    def play(self):
        return f'Playing MP3 File: '
    
class ACCFile(AudioFile):
    def play(self):
        return f'Playing ACC File: '
    
class FLACFile(AudioFile):
    def play(self):
        return f'Playing FLAC File: '
    
class Song():
    def __init__(self, song_name, file):
        self.__song_name = song_name
        self.__file = file
    
    def play(self):
        return f'{self.__file.play()} {self.__song_name}'
    
    @property
    def song_name(self):
        return self.__song_name
    
class PodcastEpisode:
    def __init__(self, episode_no, episode_name, file):
        self.__episode_no = episode_no
        self.__episode_name = episode_name
        self.__file = file
    
    def play(self):
        return f'{self.__file.play()} {self.__episode_name}'
    
    @property
    def episode_name(self):
        return self.__episode_name
    
class PodcastChanel:
    def __init__(self, chanel_name, host_name):
        self.__chanel_name = chanel_name
        self.__host_name = host_name
        self.__episode_list = []

    def get_episode_by_episode_name(self, episode_name):
        for episode in self.__episode_list:
            if episode.episode_name == episode_name:
                return episode
        raise ValueError("Episode not found")
    
    def add_episode(self, episode_no, episode_name, file):
        new_episode = PodcastEpisode(episode_no, episode_name, file)
        self.__episode_list.append(new_episode)
    
    def play(self):
        return "\n".join([episode.play() for episode in self.__episode_list])
    
    @property
    def chanel_name(self):
        return self.__chanel_name
    
class Album:
    def __init__(self, album_name):
        self.__album_name = album_name
        self.__song_list = []
    
    def get_song_by_song_name(self, song_name):
        for song in self.__song_list:
            if song.song_name == song_name:
                return song
        return None

    def add_song_to_album(self, song_name, file):
        new_song = Song(song_name, file)
        self.__song_list.append(new_song)

    def play(self):
        return "\n".join([song.play() for song in self.__song_list])
    
    @property
    def album_name(self):
        return self.__album_name
    
class Artist:
    def __init__(self, artist_name):
        self.__artist_name = artist_name
        self.__album_list = []

    def add_album(self, album_name):
        new_album = Album(album_name)
        self.__album_list.append(new_album)

    def get_album_by_album_name(self, album_name):
        for album in self.__album_list:
            if album.album_name == album_name:
                return album
        return None
    
    @property
    def artist_name(self):
        return self.__artist_name
    
    @property
    def album_list(self):
        return self.__album_list

class Playlist:
    def __init__(self, playlist_name):
        self.__playlist_name = playlist_name
        self.__media_list = []

    def play(self):
        return "\n".join([media.play() for media in self.__media_list])
    
    def add_media(self, media):
        self.__media_list.append(media)
    
    @property
    def playlist_name(self):
        return self.__playlist_name

class MediaPlayer:
    def __init__(self) -> None:
        self.__artist_list = []
        self.__podcast_chanel_list = []
        self.__playlist = []

    def play_song(self, album_name, artist_name, song_name):
        artist = self.get_artist_by_artist_name(artist_name)
        if artist:
            album = artist.get_album_by_album_name(album_name)
            if album:
                return album.get_song_by_song_name(song_name).play()
            
    def play_podcast(self, episode_name, chanel_name):
        podcast_chanel = self.get_podcast_chanel_by_name(chanel_name)
        if podcast_chanel:
            episode = podcast_chanel.get_episode_by_episode_name(episode_name)
            return episode.play()

    def play_album(self, album_name, artist_name):
        artist = self.get_artist_by_artist_name(artist_name)
        if artist:
            album = artist.get_album_by_album_name(album_name)
            return album.play()

    def play_playlist(self, playlist_name):
        playlist = self.get_playlist_by_playlist_name(playlist_name)
        if playlist:
            return playlist.play()

    def search_song(self, query):
        for artist in self.__artist_list:
            album = artist.get_album_by_album_name(query)
            if album:
                return album.play()
            
            for album in artist.album_list:
                song = album.get_song_by_song_name(query)
                if song:
                    return song.play()

    def add_artist(self, artist_name):
        new_artist = Artist(artist_name)
        self.__artist_list.append(new_artist)

    def get_artist_by_artist_name(self, artist_name):
        for artist in self.__artist_list:
            if artist.artist_name == artist_name:
                return artist
        return None

    def add_song(self, artist_name, album_name, song_name, file):
        artist = self.get_artist_by_artist_name(artist_name)
        if artist:
            album = artist.get_album_by_album_name(album_name)
            if album:
                album.add_song_to_album(song_name, file)
                return
            
    def add_album(self, artist_name, album_name):
        artist = self.get_artist_by_artist_name(artist_name)
        if artist:
            artist.add_album(album_name)

    def add_podcast_chanel(self, chanel_name, host_name):
        new_podcast_chanel = PodcastChanel(chanel_name, host_name)
        self.__podcast_chanel_list.append(new_podcast_chanel)

    def add_podcast_episode(self, chanel_name, episode_no, episode_name, file):
        podcast_chanel = self.get_podcast_chanel_by_name(chanel_name)
        if podcast_chanel:
            podcast_chanel.add_episode(episode_no, episode_name, file)

    def get_podcast_chanel_by_name(self, name):
        for podcast_chanel in self.__podcast_chanel_list:
            if podcast_chanel.chanel_name == name:
                return podcast_chanel
        return None
    
    def add_playlist(self, playlist_name):
        new_playlist = Playlist(playlist_name)
        self.__playlist.append(new_playlist)

    def get_playlist_by_playlist_name(self, playlist_name):
        for playlist in self.__playlist:
            if playlist.playlist_name == playlist_name:
                return playlist
        return None

    def add_song_to_playlist(self, artist_name, album_name, song_name, target_playlist_name):
        target_playlist = self.get_playlist_by_playlist_name(target_playlist_name)
        if not target_playlist:
            raise ValueError("Playlist not found")
        
        artist = self.get_artist_by_artist_name(artist_name)
        if artist:
            album = artist.get_album_by_album_name(album_name)
            if album:
                target_playlist.add_media(album.get_song_by_song_name(song_name))

    def add_podcast_episode_to_playlist(self, podcast_chanel_name, podcast_episode_name, target_playlist_name):
        target_playlist = self.get_playlist_by_playlist_name(target_playlist_name)
        if not target_playlist:
            raise ValueError("Playlist not found")
        
        podcast_chanel = self.get_podcast_chanel_by_name(podcast_chanel_name)
        if podcast_chanel:
            target_playlist.add_media(podcast_chanel.get_episode_by_episode_name(podcast_episode_name))
        
player = MediaPlayer()

mp3 = MP3File()
flac = FLACFile()
acc = ACCFile()

player.add_artist("Ed Sheeran")

player.add_album(artist_name="Ed Sheeran", album_name="Shape of You")
player.add_song(artist_name="Ed Sheeran", album_name="Shape of You", song_name="Shape of You", file=mp3)
player.add_song(artist_name="Ed Sheeran", album_name="Shape of You", song_name="Shape of You - Acoustic", file=mp3)

player.add_album(artist_name="Ed Sheeran", album_name="=")
player.add_song(artist_name="Ed Sheeran", album_name="=", song_name="Bad Habits", file=mp3)
player.add_song(artist_name="Ed Sheeran", album_name="=", song_name="Shivers", file=flac)

player.add_podcast_chanel(chanel_name="Lex Fridman Podcast", host_name="Lex Fridman")
player.add_podcast_episode(chanel_name="Lex Fridman Podcast", episode_no=1, episode_name="Yann Lecun", file=acc)
player.add_podcast_episode(chanel_name="Lex Fridman Podcast", episode_no=2, episode_name="Elon Musk", file=mp3)

player.add_playlist(playlist_name="1")
player.add_song_to_playlist(artist_name="Ed Sheeran", album_name="=", song_name="Bad Habits", target_playlist_name="1")
player.add_podcast_episode_to_playlist(podcast_chanel_name="Lex Fridman Podcast", podcast_episode_name="Yann Lecun", target_playlist_name="1")
player.add_podcast_episode_to_playlist(podcast_chanel_name="Lex Fridman Podcast", podcast_episode_name="Elon Musk", target_playlist_name="1")

# ! TEST CASE

# Testcase 1 : เล่นเพลง โดยส่ง instance ของเพลง และ instance ของ podcast
# Expected output 
# Playing MP3 file :  Shape of You
# Playing aac file :  Yann Lecun
print("Testcase 1 : เล่นเพลง โดยส่ง instance ของเพลง และ instance ของ podcast")
print(player.play_song(album_name="Shape of You",artist_name="Ed Sheeran",song_name="Shape of You"))
print(player.play_podcast(episode_name="Yann Lecun", chanel_name="Lex Fridman Podcast"))
print()

# Testcase 2 : เล่นเพลงใน Playlist โดยแสดงชื่อของ media ใน playlist ตามลำดับ
# Expected output
# Playing MP3 file :  Bad Habits
# Playing MP3 file :  Elon Musk

# ! โจทย์กับ Testcase ไม่เหมือนกัน จึงเพิ่ม Podcast episode "Elon Musk" ลงไปใน Playlist "1"
print("Testcase 2 : เล่นเพลงใน Playlist โดยแสดงชื่อของ media ใน playlist ตามลำดับ")
print(player.play_playlist("1"))
print()

# Testcase 3 : เล่นเพลงใน Album โดยแสดงชื่อของ media ใน Album ตามลำดับ
# Expected output
# Playing MP3 file :  Shape of You
# Playing MP3 file :  Shape of You - Acoustic
print("Testcase 3 : เล่นเพลงใน Album โดยแสดงชื่อของ media ใน Album ตามลำดับ")
print(player.play_album("Shape of You", "Ed Sheeran"))
print()

# Testcase 4 : ค้นหาเพลง
# Expected output
# Playing MP3 file :  Bad Habits
# Playing MP3 file :  Shape of You
# Playing MP3 file :  Shape of You - Acoustic
print("Testcase 4 : ค้นหาเพลง")
print(player.search_song("Bad Habits"))
print(player.search_song("Shape of You"))
