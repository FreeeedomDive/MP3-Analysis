import mp3

file = None
print("Input name of MP3-file")
filename = input()
if filename[len(filename) - 4:] != ".mp3":
    print("It is not .mp3 file!")
    filename = ""
else:
    try:
        file = mp3.MP3(filename)
    except FileNotFoundError:
        print("File not found!")
        filename = ""

print(file.track)
