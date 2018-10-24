import constants


class Parser:

    def __init__(self):
        pass

    @staticmethod
    def parse_id3v1(tags):
        tag = tags[0:3].decode("cp1251")
        if tag == "TAG":
            top = "TAG"
            name = tags[3:33].decode("UTF-8")
            artist = tags[33:63].decode("UTF-8")
            album = tags[63:93].decode("UTF-8")
            year = tags[93:97].decode("UTF-8")
            commentary = tags[97:125].decode("UTF-8")
            number = tags[126]
            genre_number = tags[127]
            genre = constants.genres[genre_number]
        else:
            top = "NO"
            name = ""
            artist = ""
            album = ""
            year = ""
            commentary = ""
            number = ""
            genre_number = ""
            genre = ""

        return {
            "top": top,
            "name": name,
            "artist": artist,
            "album": album,
            "year": year,
            "commentary": commentary,
            "number": number,
            "genre_number": genre_number,
            "genre": genre
        }
