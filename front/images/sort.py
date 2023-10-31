import pathlib
import os 
import shutil


FILES_LIST: list = []

def get_files():
    os.path.exists
    path = pathlib.Path("./")
    if path.exists():
        FILES_LIST = list(path.glob("*.png"))

def sort_files():
    return sorted(FILES_LIST, key=lambda item: item.name)
    # sorted_files = sorted(FILES_LIST, key=lambda item: item.name)
    # for i in sorted_files:
    #     print(i.name)

def main():
    get_files()
    sorted_files = sort_files()


if __name__ == '__main__':
    main()