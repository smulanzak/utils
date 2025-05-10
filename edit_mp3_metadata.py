import os
import sys
from mutagen.easyid3 import EasyID3 # pip install mutagen

PATH = r''

def edit_metadata(path: str) -> None:
    info = path.split('\\')
    artist = info[-2]
    album = info[-1][7:]
    year = info[-1][1:5]
    for file in (directory := os.listdir(path)):
        if file.endswith('.mp3'):
            tracknumber = str(int(file[:2]))
            title = file[5:-4]
            data = EasyID3(f'{path}\\{file}')
            data["artist"] = artist
            data["album"] = album
            data["date"] = year
            data["title"] = title
            data["tracknumber"] = f'{tracknumber}/{len(directory)}'
            data.save()

def main() -> None:
    edit_metadata(sys.argv[1] if len(sys.argv) == 2 else PATH)

if __name__ == "__main__":
    main()