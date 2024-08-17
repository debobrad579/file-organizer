from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer
from time import sleep

from extensions import watch_path
from organizer import move_files


class EventHandler(FileSystemEventHandler):
    def __init__(self):
        move_files()

    def on_modified(self, event):
        move_files()


def main():
    event_handler = EventHandler()

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
