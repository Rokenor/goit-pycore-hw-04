import sys
from pathlib import Path
from colorama import Fore, Style

def check_path(current_path, level=0):
    path = Path(current_path)
    shift = " "*level

    if path.is_dir():
        print(f"{shift}{Fore.BLUE}{path.name}{Style.RESET_ALL}")
        for entry in path.iterdir():
            check_path(entry, level+4)
    elif path.is_file():
        print(f"{shift}{Fore.GREEN}{path.name}{Style.RESET_ALL}")
    else:
        print(f'{Fore.RED}Something wrong. Path "{current_path}" doesn\'t exist{Style.RESET_ALL}')

if __name__ == "__main__":
    path_for_check = sys.argv[1]
    check_path(path_for_check)
