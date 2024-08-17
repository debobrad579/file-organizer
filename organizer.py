from datetime import datetime
from time import ctime
import os

from extensions import get_subfolder_root, watch_path, destination_root, subfolder_roots, download_extensions
from months import months


def get_month_folder(root, file_path):
    date_of_created = datetime.strptime(ctime(os.path.getmtime(file_path)), "%a %b %d %H:%M:%S %Y")
    print(date_of_created)
    destination = f"{root}/{date_of_created.year}/{months[str(date_of_created.month)]}"

    if not os.path.exists(destination):
        os.makedirs(destination)

    return destination


def rename_file_if_exists(location, filename, file_extension):
    file_number = 0
    new_filename = filename

    while True:
        if not os.path.exists(f"{location}/{new_filename}{file_extension}"):
            break
        
        file_number += 1
        new_filename = f"{filename} ({file_number})"

    return new_filename


def move_files():
    for file in os.listdir(watch_path):
        file_path = f"{watch_path}/{file}"
        filename, file_extension = os.path.splitext(file)
        file_extension = file_extension.lower()

        if file in subfolder_roots or file_extension in download_extensions or filename == ".com.google.Chrome":
            continue
            
        destination = get_month_folder(f"{destination_root}/{get_subfolder_root(file_extension)}", file_path)
        new_filename = rename_file_if_exists(destination, filename, file_extension)
        new_file_path = f"{destination}/{new_filename}{file_extension}"
        os.rename(file_path, new_file_path)

        print(f"Moved '{file_path}' to '{new_file_path}'")
