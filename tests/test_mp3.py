import unittest
from src import mp3


class MP3Test(unittest.TestCase):

    def test_no_id3v1(self):
        test_file = mp3.MP3("../Files/Maduk, Veela - Ghost Assassin (Original "
                            "Mix).mp3")
        self.assertEqual(test_file.id3v1_tags["top"], "NO")

    def test_id3v2(self):
        test_file = mp3.MP3("../Files/Maduk, Veela - Ghost Assassin (Original "
                            "Mix).mp3")
        self.assertTrue(test_file.contains_lyrics)
        self.assertTrue(test_file.contains_album_picture)
        self.assertEqual(test_file.id3v2_tags["TIT2"],
                         "Ghost Assassin (Original Mix)")
        self.assertEqual(test_file.id3v2_tags["TPE2"], "Maduk")
        self.assertEqual(len(test_file.id3v2_tags), 10)

    def test_no_id3v1_id3v2(self):
        test_file = mp3.MP3("../Files/NIVIRO - The Guardian of Angels.mp3")
        self.assertEqual(test_file.id3v1_tags["top"], "NO")
        self.assertEqual(len(test_file.id3v2_tags), 0)
