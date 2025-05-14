import os
import sys

PATH = r''

def remove_tag(path: str) -> None:
    for file in os.listdir(path):
        source = f'{path}\\{file}'
        if file.endswith('.mp3'):
            parts = file.split(' ')
            if parts[-1][0] == '[' and parts[-1][-5] == ']':
                dest = f"{path}\\{' '.join(parts[:-1])}".strip()
                os.rename(source, f'{dest}.mp3')

def main() -> None:
    remove_tag(sys.argv[1] if len(sys.argv) == 2 else PATH)

if __name__ == "__main__":
    main()