import json


def load(file_name):  
    file_path = f'gendiff/files/{file_name}'
    
    with open(file_path) as f1:
        result = json.load(f1)

    return result


def get_data_format(file_name):
    ext = Path(file_name).suffix.lower()
    if ext in ['.json']:
        return 'json'
    elif ext in ['.yaml', '.yml']:
        return 'yaml'
    