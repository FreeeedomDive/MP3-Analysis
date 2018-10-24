import mp3
import sys
from pygame import mixer


class CLI:

    def __init__(self):
        self.file = None

    def start(self):
        mainloop = True
        filename = ""
        while filename == "":
            print("Input name of MP3-file")
            filename = input()
            if filename[len(filename) - 4:] != ".mp3":
                print("It is not .mp3 file!")
                filename = ""
            else:
                try:
                    self.file = mp3.MP3(filename)
                except FileNotFoundError:
                    print("File not found!")
                    filename = ""
        while mainloop:
            print("Enter command for mp3-file")
            command = input()
            self.execute(command)

    def execute(self, command):
        if command == "exit":
            sys.exit(0)
        if command == "help":
            print("COMMANDS:")
            print("\tparse: Get tags from mp3 file")
            print("\tplay: Launch player and start playing music")
            print("\texit: Exit from program")
        elif command == "parse":
            self.file.parse_id3v1()
            print(self.file.id3v1_string)
        elif command == "play":
            self.player_control()
        else:
            print("Unexpected command")

    def player_control(self):
        print("PLAYER")
        print("Now playing: {0}".format(self.file.filename))
        mixer.init()
        mixer.music.load(self.file.filename)
        mixer.music.play()
        secondloop = True
        on_pause = False
        while secondloop:
            print("Enter command for player")
            command = input()
            if command == "help":
                print("PLAYER:")
                print("\tpause: Pause music")
                print("\tunpause: Continue music")
                print("\tvolume: Change volume")
                print("\treturn: Return to main control")
            elif command == "pause":
                mixer.music.pause()
                on_pause = True
            elif command == "unpause":
                if on_pause:
                    mixer.music.unpause()
                    on_pause = False
            elif command == "volume":
                print("Set value of volume in the gap [0, 1]")
                print("Current volume: {0}".format(mixer.music.get_volume()))
                value = float(input())
                mixer.music.set_volume(value)
            elif command == "return":
                mixer.music.stop()
                mixer.quit()
                return
            else:
                print("Unexpected command for player")
