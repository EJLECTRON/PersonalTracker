import sys
from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QListWidget
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
from os import getenv
import webbrowser

load_dotenv()


class MusicPlayer(QMainWindow):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.sp = self.authenticate_spotipy()

    def init_ui(self):
        self.setWindowTitle("My Music Player")
        self.setGeometry(100, 100, 400, 400)
        self.search_input = QLineEdit(self)
        self.search_input.setGeometry(50, 50, 250, 30)
        search_button = QPushButton("Search", self)
        search_button.setGeometry(300, 50, 80, 30)
        search_button.clicked.connect(self.search_music)
        self.result_list = QListWidget(self)
        self.result_list.setGeometry(50, 100, 330, 200)
        play_button = QPushButton("Play", self)
        play_button.setGeometry(50, 320, 80, 30)
        play_button.clicked.connect(self.play_selected_track)

    def authenticate_spotipy(self):
        spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=getenv("SPOTIFY_WIDGET_CLIENT_ID"),
                                                       client_secret=getenv("SPOTIFY_WIDGET_CLIENT_SECRET"),
                                                       redirect_uri=getenv("APP_REDIRECT"),
                                                       scope='user-modify-playback-state'))
        oath = spotipy.SpotifyOAuth(client_id=getenv("SPOTIFY_WIDGET_CLIENT_ID"),
                                    client_secret=getenv("SPOTIFY_WIDGET_CLIENT_SECRET"),
                                    redirect_uri=getenv("APP_REDIRECT"))
        token_dict = oath.get_cached_token()
        token = token_dict['access_token']
        spotifyObject = spotipy.Spotify(auth=token)
        return spotifyObject

    def search_music(self):
        query = self.search_input.text()

        if query:
            results = self.sp.search(q=query, type='track', limit=10)
            self.result_list.clear()

            for track in results['tracks']['items']:
                self.result_list.addItem(f"{track['name']} - {track['artists'][0]['name']} ({track['uri']})")

    def play_selected_track(self):
        selected_item = self.result_list.currentItem()
        if selected_item:
            track_uri = selected_item.text().split(' (')[1][:-1]
            print(track_uri)
            webbrowser.open(track_uri)
            self.sp.start_playback(uris=[track_uri])
            print(f"Playing music: {selected_item.text().split(' (')[0]}")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MusicPlayer()
    window.show()
    sys.exit(app.exec_())