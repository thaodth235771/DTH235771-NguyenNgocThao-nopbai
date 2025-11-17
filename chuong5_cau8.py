import os

def get_filename(path):
    return os.path.basename(path)

def get_song_name(path):
    filename = os.path.basename(path)
    name, ext = os.path.splitext(filename)
    return name

# Test
path = input("Nhập đường dẫn bài hát: ")

print("Tên file:", get_filename(path))
print("Tên bài hát:", get_song_name(path))
