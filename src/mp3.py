import os
import src.tags_parser as p
import src.constants as constants
from PIL import Image


class MP3:

    def __init__(self, path):
        self.path = path
        path_arr = path.split('\\')
        self.filename = path_arr[len(path_arr) - 1]
        self.size = os.path.getsize(path)
        file = open(path, 'rb')
        self.track = file.read(self.size - 128)
        self.id3v1_bytes = file.read()
        self.id3v1_tags = {}
        self.id3v2_tags = {}
        self.id3v1_string = ""
        self.id3v2_string = ""
        self.contains_album_picture = False
        self.picture = None
        self.contains_lyrics = False
        self.lyrics = """"""
        file.close()

    def parse_id3v1(self):
        self.id3v1_tags = p.Parser.parse_id3v1(self.id3v1_bytes)
        self.id3v1_string = self.create_string_with_id3v1()

    def create_string_with_id3v1(self):
        if self.id3v1_tags["top"] == "NO":
            return "No id3v1 tags for this mp3-file"
        return '''=========================
ID3V1 TAGS
  Artist: {0}
  Name: {1}
  Album: {2}
  Number in album: {3}
  Year: {4}
  Genre: {5}
  Comment: {6}
========================='''.format(self.id3v1_tags["artist"],
                                    self.id3v1_tags["name"],
                                    self.id3v1_tags["album"],
                                    self.id3v1_tags["number"],
                                    self.id3v1_tags["year"],
                                    self.id3v1_tags["genre"],
                                    self.id3v1_tags["commentary"])

    def parse_id3v2(self):
        self.id3v2_tags = p.Parser.parse_id3v2(self.track)
        self.id3v2_string = self.create_string_with_id3v2()

    def create_string_with_id3v2(self):
        if self.id3v2_tags.get("tag") is not None:
            return "No id3v2 tags for this mp3-file"
        tags = []
        for tag in self.id3v2_tags:
            temp = constants.FRAMES.get(tag)
            if temp is not None:
                info = temp
            else:
                info = "No info"
            if tag == "APIC":
                content = "*file contains the cover of album*"
                # self.has_album_picture = True
                # self.picture = Image.frombytes('RGBA', (200, 200),
                #                                bytes(self.id3v2_tags[tag]))
            elif tag == "USLT":
                content = "*file contains the lyrics of track*"
                self.contains_lyrics = True
                self.lyrics = self.id3v2_tags[tag]
            elif tag == "TCON":
                if self.id3v2_tags[tag] == 'RX':
                    content = "Remix"
                elif self.id3v2_tags[tag] == 'CR':
                    content = 'Cover'
                else:
                    content = self.id3v2_tags[tag]

            else:
                content = self.id3v2_tags[tag]
            tags.append("  {0} - {1}: {2}".format(tag, info, content))
        result = "=========================\nID3V2 TAGS\n"
        for i in range(0, len(tags)):
            result += tags[i] + "\n"
        result += "========================="
        return result
