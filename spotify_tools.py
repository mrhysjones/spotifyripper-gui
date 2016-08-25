from __future__ import unicode_literals

import sys
import threading
import os
import spotify

# Assuming a spotify_appkey.key in the current dir
session = spotify.Session()

# Process events in the background
loop = spotify.EventLoop(session)
loop.start()

# Events for coordination
logged_in = threading.Event()

def on_connection_state_updated(session):
    if session.connection.state is spotify.ConnectionState.LOGGED_IN:
        logged_in.set()

# Register event listeners
session.on(
    spotify.SessionEvent.CONNECTION_STATE_UPDATED, on_connection_state_updated)

session.login('1994mattj@gmail.com', 'uganda2014')

logged_in.wait()

def get_session():
    return session

def keyword_search(words):
    search = session.search(words, track_count=250)
    search.load()
    return search

def load_playlist(playlist):
    playlist = session.get_playlist(playlist, track_count=250)
    playlist.load()
    return playlist

def load_album(album):
    album = session.get_album(album, track_count=250)
    album.load()
    return album

def load_artist(artist):
    artist = session.get_artist(artist, track_count=250)
    artist.load()
    return artist

def load_track(track):
    track = session.get_track(track)
    track.load()
    return track

def duration_string(dur):
    total_seconds = dur / 1000
    minutes = total_seconds/60
    seconds = total_seconds % 60
    mm_ss = str(minutes) + 'm' + str(seconds) + 's'
    return mm_ss

def download_track(uri):
    os.system('python spotify_ripper/main.py ' + uri)
