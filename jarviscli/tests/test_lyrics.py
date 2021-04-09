import unittest
from plugins.lyrics import lyrics
from tests import PluginTest

class Lyrics_Test(PluginTest):

    def setUp(self):
        self.song_name = "everybody dies"
        self.artist_name = "ayreon"
        self.complete_info = "everybody dies-ayreon"
        self.wrong_info = "everybody dies-arebon"
        self.module = self.load_plugin(lyrics)

# Test whether the parameters are completed or not
    def test_lyrics_found_given_full_parameters(self):
        self.assertIsNotNone(self.module.find(self.complete_info),
            "you forgot to put any input")

#Test if the song name parameter is incomplete
    def test_lyrics_not_found_given_incomplete_parameter_song(self):
        self.assertEqual(self.module.find("-drake"),
            "The song name parameter was incomplete")
    
#Test if the artist name parameter is incomplete
    def test_lyrics_not_found_given_incomplete_parameter_artist(self):
        self.assertEqual(self.module.find("jungle-"),
            "The artist name parameter was incomplete")

#Test if program can find the lyrics to the song Jungle by drake
    def test_lyrics_found_given_complete_parameters(self):
        file = open("tests/jungle_lyrics.txt", "r")
        jungle_lyrics = file.read()
        file.close()
        self.assertIsNotNone(self.module.find("jungle-drake"),
            jungle_lyrics)

#Test if the program can find the lyrics to People's Champ by Arkells if the song and artist input are misspelled
    def test_lyrics_found_given_complete_parameters(self):
        file = open("tests/peoples_arkells.txt", "r")
        peoples_arkells = file.read()
        file.close()
        self.assertIsNotNone(self.module.find("peoples chump-arkelllls"),
            peoples_arkells)

#Test if the song or singer do not exist
    def test_lyrics_not_found_given_wrong_parameter(self):
        self.assertEqual(
            self.module.find(
                self.wrong_info),
            "Song or Singer does not exist or the API does not have lyrics")

    

if __name__ == '__main__':
    unittest.main()
