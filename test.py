import mp3
import wx

app = wx.App(False)
openFileDialog = wx.FileDialog(None, "DAI MNE MP3", "", "",
                               "MP3 Files (*.mp3)|*.mp3")
openFileDialog.ShowModal()
print(openFileDialog.GetPath())
openFileDialog.Destroy()
