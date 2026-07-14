import json
import yaml
from pathlib import Path


def load(file_name):  
    file_path = f'gendiff/files/{file_name}'
    
    fmt = get_data_format(file_name)
    
    with open(file_path) as f:
        if fmt == "json":
            return json.load(f)
        elif fmt == "yaml":
            return yaml.safe_load(f)


def get_data_format(file_name):
    ext = Path(file_name).suffix.lower()
    if ext in ['.json']:
        return 'json'
    elif ext in ['.yaml', '.yml']:
        return 'yaml'
    