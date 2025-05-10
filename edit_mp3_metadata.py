import os
import sys
from mutagen.easyid3 import EasyID3 # pip install mutagen

PATH = r''

def edit_metadata(path: str) -> None:
    info = path.split('\\')
    if len(info) >= 2:
        artist = info[-2]
        album = info[-1][7:]
        year = info[-1][1:5]
        if info[-1].split(' ')[0] == f'({int(year)})':
            directory = os.listdir(path)
            number_of_tracks = len([file for file in directory if file.endswith('.mp3')])
            for file in directory:
                if file.endswith('.mp3'):
                    tracknumber = str(int(file[:2]))
                    title = file[5:-4]
                    data = EasyID3(f'{path}\\{file}')
                    data["artist"] = artist
                    data["album"] = album
                    data["date"] = year
                    data["title"] = title
                    data["tracknumber"] = f'{tracknumber}/{number_of_tracks}'
                    data.save()

def main() -> None:
    edit_metadata(sys.argv[1] if len(sys.argv) == 2 else PATH)

if __name__ == "__main__":
    main()