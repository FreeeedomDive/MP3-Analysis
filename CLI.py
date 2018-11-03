import mp3
import sys
from pygame import mixer
import wx


class CLI:

    def __init__(self):
        self.file = None

    def execute(self, command):
        if command == "exit":
            sys.exit(0)
        if command == "help":
            print("COMMANDS:")
            print("\tparse: Get tags from mp3 file")
            print("\tplay: Launch player and start playing music")
            print("\texit: Exit from program")
        elif command == "parse_id3v1":
            self.file.parse_id3v1()
            print(self.file.id3v1_string)
        elif command == "parse_id3v2":
            self.file.parse_id3v2()
        elif command == "play":
            self.player_control()
        else:
            print("Unexpected command")

    def start(self):
        mainloop = True
        app = wx.App(False)
        openFileDialog = wx.FileDialog(None, "DAI MNE MP3", "", "",
                                       "MP3 Files (*.mp3)|*.mp3")
        if openFileDialog.ShowModal() == wx.ID_CANCEL:
            print("No selected file")
            sys.exit(0)
        path = openFileDialog.GetPath()
        pathh = path.split('\\')
        filename = pathh[len(pathh) - 1]
        print(filename)
        openFileDialog.Destroy()
        self.file = mp3.MP3(path)
        while mainloop:
            print("Enter command for mp3-file")
            command = input()
            self.execute(command)

    def player_control(self):
        print("PLAYER")
        print("Now playing: {0}".format(self.file.filename))
        mixer.init()
        mixer.music.load(self.file.path)
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
