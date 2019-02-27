import json
import os

RESOURCE_PATH = f'.\\resources\\'

def save_file(name, extension='.json', data=''):
    if os.path.isfile(RESOURCE_PATH + name + extension):
        os.remove(RESOURCE_PATH + name + extension)
        with open(RESOURCE_PATH + name + extension, mode='w') as file:
            file.write(data)
    else:
        with open(RESOURCE_PATH + name + extension, mode='w+') as file:
            file.write(data)

def read_file(name, extension='.json'):
    with open(RESOURCE_PATH + name + extension) as file_data:
        data = json.load(file_data)
    return data
