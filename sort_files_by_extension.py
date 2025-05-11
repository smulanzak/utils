import os
import shutil
import sys

SOURCE = r""
FOLDERS = ["images",
           "pdfs",
           "executables",
           "texts",
           "xlsxs",
           "csvs",
           "zips",
           "songs",
           "videos",
           "htmls",
           "guitar-tabs",
           "torrent-files",
           "midis"]

def sort_files(source: str, folders: list[str]) -> None:
    mkdirs(source, folders)
    move_files(source)
    rmdirs(source)

def mkdirs(source: str, folders: str) -> None:
    for folder in folders:
        path = f"{source}\\{folder}"
        if not os.path.exists(path):
            os.makedirs(path)

def move_files(source: str) -> None:
    for file in os.listdir(source):
        if not os.path.isdir(file):
            path = f"{source}\\{file}"
            match file.split('.')[-1]:
                case "pdf":
                    shutil.move(path, f"{source}\\pdfs\\{file}")
                case "jpg" | "png" | "jpeg" | "webp":
                    shutil.move(path, f"{source}\\images\\{file}")
                case "exe" | "msi":
                    shutil.move(path, f"{source}\\executables\\{file}")
                case "csv":
                    shutil.move(path, f"{source}\\csvs\\{file}")
                case "xlsx":
                    shutil.move(path, f"{source}\\xlsxs\\{file}")
                case "zip" | "rar" | "7z":
                    shutil.move(path, f"{source}\\zips\\{file}")
                case "mp3" | "wma":
                    shutil.move(path, f"{source}\\songs\\{file}")
                case "mp4" | "avi" | "mov":
                    shutil.move(path, f"{source}\\videos\\{file}")
                case "html":
                    shutil.move(path, f"{source}\\htmls\\{file}")
                case "txt" | "docx" | "dotx" | "doc":
                    shutil.move(path, f"{source}\\texts\\{file}")
                case "ptb" | "gp3" | "gp4" | "gp5" | "gpx":
                    shutil.move(path, f"{source}\\guitar-tabs\\{file}")
                case "torrent":
                    shutil.move(path, f"{source}\\torrent-files\\{file}")
                case "mid":
                    shutil.move(path, f"{source}\\midis\\{file}")

def rmdirs(source: str) -> None:
    for folder in os.listdir(source):
        path = f"{source}\\{folder}"
        if os.path.isdir(path) and len(os.listdir(path)) == 0:
            os.rmdir(path)

def main() -> None:
    sort_files(sys.argv[1] if len(sys.argv) == 2 else SOURCE, FOLDERS)

if __name__ == "__main__":
    main()