extensions = {
# Audio
    ".aif": "Audio",
    ".cda": "Audio",
    ".flac": "Audio",
    ".mid": "Audio",
    ".midi": "Audio",
    ".mp3": "Audio",
    ".mpa": "Audio",
    ".m3u": "Audio",
    ".ogg": "Audio",
    ".wav": "Audio",
    ".wma": "Audio",
    ".wpl": "Audio",
# Executables
    ".apk": "Executables",
    ".bat": "Executables",
    ".com": "Executables",
    ".exe": "Executables",
    ".gadget": "Executables",
    ".jar": "Executables",
    ".wsf": "Executables",
# Folders
    ".7z": "Folders/Compressed Folders",
    ".arj": "Folders/Compressed Folders",
    ".deb": "Folders/Compressed Folders",
    ".pkg": "Folders/Compressed Folders",
    ".rar": "Folders/Compressed Folders",
    ".rpm": "Folders/Compressed Folders",
    ".z": "Folders/Compressed Folders",
    ".zip": "Folders/Compressed Folders",
    "": "Folders/Extracted Folders",
# Images
    ".ai": "Images",
    ".bmp": "Images",
    ".cr2": "Images",
    ".gif": "Images",
    ".ico": "Images",
    ".icns": "Images",
    ".jpg": "Images",
    ".jpeg": "Images",
    ".png": "Images",
    ".ps": "Images",
    ".pds": "Images",
    ".svg": "Images",
    ".tif": "Images",
    ".tiff": "Images",
    ".webp": "Images",
# Text
    ".txt": "Text",
    ".doc": "Text",
    ".docx": "Text",
    ".odt": "Text",
    ".pdf": "Text",
    ".rtf": "Text",
    ".tex": "Text",
    ".wks": "Text",
    ".wps": "Text",
    ".wpd": "Text",
    ".fnt": "Text",
    ".fon": "Text",
    ".otf": "Text",
    ".ttf": "Text",
    ".key": "Text",
    ".odp": "Text",
    ".pps": "Text",
    ".ppt": "Text",
    ".pptx": "Text",
    ".ods": "Text",
    ".xlr": "Text",
    ".xls": "Text",
    ".xlsx": "Text",
# Videos
    ".3g2": "Videos",
    ".3gp": "Videos",
    ".avi": "Videos",
    ".flv": "Videos",
    ".h264": "Videos",
    ".m4v": "Videos",
    ".mkv": "Videos",
    ".mov": "Videos",
    ".mp4": "Videos",
    ".mpg": "Videos",
    ".mpeg": "Videos",
    ".rm": "Videos",
    ".swf": "Videos",
    ".vob": "Videos",
    ".wmv": "Videos"
}

download_extensions = [".download", ".crdownload", ".tmp", ".ini"]
subfolder_roots = ["Audio", "Executables", "Folders", "Images", "Other", "Text", "Videos"]
watch_path = "/home/debobrad579/Downloads"
destination_root = "/home/debobrad579/Downloads"


def get_subfolder_root(file_extension):
    try: return extensions[file_extension]
    except KeyError: return "Other"
