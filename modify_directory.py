import os
import sys
from mutagen.easyid3 import EasyID3 # pip install mutagen

PATH = r''

def remove_tag(path: str) -> None:
    for file in os.listdir(path):
        source = f'{path}\\{file}'
        if file.endswith('.mp3'):
            parts = file.split(' ')
            if parts[-1][0] == '[' and parts[-1][-5] == ']':
                dest = f"{path}\\{' '.join(parts[:-1])}".strip()
                os.rename(source, f'{dest}.mp3')

def add_tracknumber_to_file(path: str) -> None:
    files = [f"{path}\\{file}" for file in os.listdir(path) if not os.path.isdir(f"{path}\\{file}")]
    file_data = [(file, os.path.getctime(file)) for file in files]
    for i, file_data in enumerate(sorted(file_data, key=lambda x: x[1]), 1):
        track_name = file_data[0].split("\\")[-1]
        if not track_name.endswith('.mp3') or (track_name[0].isdigit() and track_name[1].isdigit()):
            continue
        path = f"{file_data[0].split(track_name)[0]}"
        os.rename(file_data[0], f"{path}\\{'0'+str(i) if i < 10 else str(i)} - {track_name}")

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

def run(path: str) -> None:
    remove_tag(path)
    add_tracknumber_to_file(path)
    edit_metadata(path)

def main() -> None:
    path = sys.argv[1] if len(sys.argv) >= 2 else PATH
    if len(sys.argv) == 3:
        if sys.argv[2] != '--all':
            raise ValueError(f"Invalid input argument used, expected: '--all', got: '{sys.argv[2]}'")
        for dir in os.listdir(sys.argv[1]):
            run(f"{path}\\{dir}")
    else:
        run(path)

if __name__ == "__main__":
    main()