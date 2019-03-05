import json
from pathlib import Path

RESOURCE_FOLDER = Path("./resources/")

def save_file(name, extension='.json', data=''):
    file = RESOURCE_FOLDER / (name + extension)
    if file.exists():
        file.unlink();
        file.write_text(data)
    else:
        file.write_text(data)

def read_file(name, extension='.json'):
    file = RESOURCE_FOLDER / (name + extension)
    with open(file) as file_data:
        return json.load(file_data)
