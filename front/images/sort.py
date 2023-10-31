import pathlib
import re


PATTERN = '.*-icon.*'

FILES_LIST: list = []
ICONS: list = []

def get_icons():
    path = pathlib.Path("./")
    if path.exists():
        icons = list(path.glob("*-icon*"))
        with open('Icons.txt', 'w') as f:
            icon_names = list(map(lambda i: i.name, icons))


            # new_list = []
            # for item in icon_names:
            #     new_list.append(item.upper())
            # print(new_list)

            # new_list = [name.upper() for name in icon_names]
            # print(new_list)

            for item in icon_names:
                f.write(f"{item}\n")
            f.close()

def get_files():
    path = pathlib.Path("./")
    if path.exists():
        FILES_LIST = list(path.glob("*.png"))

def sort_files():
    return sorted(FILES_LIST, key=lambda item: item.name)

def main():
    get_files()
    sorted_files = sort_files()

    get_icons()


if __name__ == '__main__':
    main()