import json
from pathlib import Path

import yaml


def load(file_path):  
    fmt = get_data_format(file_path)
    
    with open(file_path) as f:
        if fmt == "json":
            return json.load(f)
        elif fmt == "yaml":
            return yaml.safe_load(f)


def get_data_format(file_path):
    ext = Path(file_path).suffix.lower()
    if ext in ['.json']:
        return 'json'
    elif ext in ['.yaml', '.yml']:
        return 'yaml'
    