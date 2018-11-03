import mp3
import sys
from pygame import mixer
import wx
import time


class CLI:

    def __init__(self):
        self.file = None

    def start(self):
        mainloop = True
        time.sleep(0.3)
        print("==========================")
        time.sleep(0.3)
        print("WELCOME TO ID3 TAGS PARSER")
        time.sleep(0.3)
        print("Commands:")
        time.sleep(0.3)
        print("\tparse_id3v1: Get id3v1 tags from mp3 file")
        time.sleep(0.3)
        print("\tparse_id3v2: Get id3v2 tags from mp3 file")
        time.sleep(0.3)
        print("\tplay: Launch player and start playing music")
        time.sleep(0.3)
        print("\tchoose_file: Choose another file")
        time.sleep(0.3)
        print("\texit: Exit from program")
        time.sleep(0.3)
        print("Now choose the file")
        time.sleep(0.3)
        path = self.choose_file()
        self.file = mp3.MP3(path)
        while mainloop:
            print("Enter command for mp3-file")
            command = input()
            self.execute(command)

    @staticmethod
    def choose_file():
        app = wx.App(False)
        open_file_dialog = wx.FileDialog(None, "DAI MNE MP3", "", "",
                                         "MP3 Files (*.mp3)|*.mp3")
        if open_file_dialog.ShowModal() == wx.ID_CANCEL:
            print("No selected file")
            sys.exit(0)
        full_path = open_file_dialog.GetPath()
        path = full_path.split('\\')
        filename = path[len(path) - 1]
        print(filename)
        open_file_dialog.Destroy()
        return filename

    def execute(self, command):
        if command == "exit":
            sys.exit(0)
        elif command == "choose_file":
            path = self.choose_file()
            self.file = mp3.MP3(path)
        elif command == "parse_id3v1":
            self.file.parse_id3v1()
            print(self.file.id3v1_string)
        elif command == "parse_id3v2":
            self.file.parse_id3v2()
            print(self.file.id3v2_string)
        elif command == "play":
            self.player_control()
        else:
            print("Unexpected command")

    def player_control(self):
        print("PLAYER (type 'help' for possible commands)")
        print("Now playing: {0}".format(self.file.filename))
        mixer.init()
        mixer.music.load(self.file.path)
        mixer.music.play()
        second_loop = True
        on_pause = False
        while second_loop:
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
