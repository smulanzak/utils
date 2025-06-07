import os
import sys
import subprocess
from mutagen.easyid3 import EasyID3 # pip install mutagen

PATH = r''
INPUTS_FILE = r''
COMMAND = 'yt-dlp -x --audio-format mp3 --audio-quality 320k '

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
        if not track_name.endswith('.mp3') or (track_name[0].isdigit() and track_name[1].isdigit() and track_name[2:5] == ' - '):
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

def download(path: str, inputs_file: str) -> None:
    directories = [f"{path}\\{directory}" for directory in os.listdir(path)]
    with open(inputs_file) as f:
        inputs = [inp.strip() for inp in f.readlines()]
    if len(directories) != len(inputs):
        raise Exception(f"Number of inputs: ({len(inputs)}) must be equal to the number of directories: ({len(directories)})")
    for i in range(len(inputs)):
        subprocess.run(COMMAND + inputs[i], cwd=directories[i])
    for directory in directories:
        run(directory)

def run(path: str) -> None:
    remove_tag(path)
    add_tracknumber_to_file(path)
    edit_metadata(path)

def main() -> None:
    path = sys.argv[1] if len(sys.argv) >= 2 else PATH
    inputs_file = sys.argv[2] if len(sys.argv) >= 4 else INPUTS_FILE
    if len(sys.argv) == 3: # Expected format: py.exe modify_directory.py parent_directory --all
        if sys.argv[2] != '--all':
            raise ValueError(f"Invalid input argument used, expected: '--all', got: '{sys.argv[2]}'")
        for dir in os.listdir(sys.argv[1]):
            run(f"{path}\\{dir}")
    elif len(sys.argv) == 4: # Expected format: py.exe modify_directory.py parent_directory inputs_file --download
        if sys.argv[3] != '--download':
            raise ValueError(f"Invalid input argument used, expected: '--download', got: '{sys.argv[3]}'")
        download(path, inputs_file)
    elif len(sys.argv) == 2: # Expected format: py.exe modify_directory.py directory
        run(path)

if __name__ == "__main__":
    main()