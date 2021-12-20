from datetime import date
import os

from extensions import get_subfolder_root
from months import months


def get_month_folder(root):
    destination = f"{root}\\{date.today().year}\\{months[str(date.today().month)]}"

    if not os.path.exists(destination):
        os.makedirs(destination)

    return destination


def rename_file_if_exists(location, filename, file_extension):
    file_number = 0
    new_filename = filename

    while True:
        if not os.path.exists(f"{location}\\{new_filename}{file_extension}"):
            break
        
        file_number += 1
        new_filename = f"{filename} ({file_number})"

    return new_filename


def get_new_file_location(filename, file_extension, destination_root):
    destination = get_month_folder(f"{destination_root}\\{get_subfolder_root(file_extension)}")
    filename = rename_file_if_exists(destination, filename, file_extension)

    return f"{destination}\\{filename}{file_extension}"
