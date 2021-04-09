# -*- coding: utf-8 -*-
import requests
import bs4
from plugin import plugin, require
from azapi import AZlyrics

@require(network=True)
@plugin('lyrics')
class lyrics():
    """
    finds lyrics
    the format is song-artist
    song and artist are separated by a -
    -- Example:
        lyrics wonderful tonight-eric clapton
    """

    def __call__(self, jarvis, s):
        jarvis.say(self.find(s))

    def find(self, s):
        info = s.split('-')

        artist = None
        song = None

        if info:
            song = info[0]
            info.pop(0)
        if info:
            artist = info[0]
            info.pop(0)
        if not song or not artist:
            # error if artist or song don't exist
            return "you forgot to add either song name or artist name"
        response = get_lyric(artist, song)
        if response:
            return response
        else:
            return "Song or Singer does not exist or the API does not have lyrics"


# makes api call to AZ lyrics and returns song result
def get_lyric(singer, song):
    API = AZlyrics('google', accuracy=0.5)
    API.artist = singer
    API.title = song
    API.getLyrics()

    return API.lyrics