import json

RESOURCE_PATH = f'.\\resources\\'

def save_file(name, extension='.json', data=''):
    with open(RESOURCE_PATH + name + extension, mode='w') as file:
        file.write(data)

def read_file(name, extension='.json'):
    with open(RESOURCE_PATH + name + extension) as file_data:
        data = json.load(file_data)
    return data
