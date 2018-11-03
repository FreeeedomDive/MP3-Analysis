import os
import parse as p


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
        file.close()

    def parse_id3v1(self):
        self.id3v1_tags = p.Parser.parse_id3v1(self.id3v1_bytes)
        self.id3v1_string = self.create_string_with_id3v1()

    def create_string_with_id3v1(self):
        if self.id3v1_tags["top"] == "NO":
            return "No id3v1 tags for this mp3-file"
        return '''=========================
ID3V1 TAGS
  File: {0}
  Artist: {1}
  Name: {2}
  Album: {3}
  Number in album: {4}
  Year: {5}
  Genre: {6}
  Comment: {7}
========================='''.format(self.filename, self.id3v1_tags["artist"],
                                    self.id3v1_tags["name"],
                                    self.id3v1_tags["album"],
                                    self.id3v1_tags["number"],
                                    self.id3v1_tags["year"],
                                    self.id3v1_tags["genre"],
                                    self.id3v1_tags["commentary"])

    def parse_id3v2(self):
        # TODO
        self.id3v2_tags = p.Parser.parse_id3v2(self.track)

    def create_string_with_id3v2(self):
        # TODO
        pass
