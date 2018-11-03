import constants
import utilities


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
            genre = constants.GENRES[genre_number]
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

    @staticmethod
    def parse_id3v2(tags):
        tag = tags[0:3].decode("ISO-8859-1")
        if tag != "ID3":
            return {"tag": "No id3v2 tags in this file"}
        version = tags[3]
        sub_version = tags[4]
        flags = tags[5]
        length = utilities.make_length_correct(int.from_bytes(
            tags[6:10], "big"))
        tags = tags[10:10 + length]
        passed = 0
        tags_dict = {}
        while passed < length:
            if tags[passed:passed + 4] == b'\x00\x00\x00\x00':
                break
            tag_name = tags[passed:passed + 4].decode('UTF-8')
            tag_info = constants.FRAMES.get(tag_name)
            tag_length = int.from_bytes(tags[passed + 4:passed + 8], "big")
            tag_flags = tags[passed + 8:passed + 10]
            tag_content = tags[passed + 10:passed + 10 + tag_length] \
                .decode("ISO-8859-1")
            passed += (10 + tag_length)
            tags_dict[tag_name] = tag_content
        return tags_dict