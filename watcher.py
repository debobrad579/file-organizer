from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from time import sleep
import os

from organizer import get_new_file_location
from extensions import subfolder_roots, download_extensions


class EventHandler(FileSystemEventHandler):
    def __init__(self, watch_path, destination_root):
        self.watch_path = watch_path
        self.destination_root = destination_root
        self.move_files()

    def on_modified(self, event):
        self.move_files()
    
    def move_files(self):
        for file in os.listdir(self.watch_path):
            filename, file_extension = os.path.splitext(file)
            file_extension = file_extension.lower()

            if filename in subfolder_roots or file_extension in download_extensions:
                continue

            new_location = get_new_file_location(filename, file_extension, self.destination_root)
            os.rename(f"{self.watch_path}\\{file}", new_location)
            
            print("")
            print(f"Moved '{self.watch_path}\\{file}' to '{new_location}'")


def main():
    watch_path = "C:\\Users\\thebr\\Downloads"
    destination_root = "C:\\Users\\thebr\\Downloads"
    event_handler = EventHandler(
        watch_path=watch_path, 
        destination_root=destination_root
    )

    observer = Observer()
    observer.schedule(event_handler, watch_path, recursive=True)
    observer.start()

    try:
        while True:
            sleep(60)
    except KeyboardInterrupt:
        observer.stop()
        
    observer.join()


if __name__ == "__main__":
    main()
