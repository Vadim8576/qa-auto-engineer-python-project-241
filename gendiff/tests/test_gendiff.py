from pathlib import Path

import pytest

from gendiff.generate_diff import generate_diff
from gendiff.load_json import load_json

BASE_DIR = Path(__file__).resolve().parent.parent
FILES_DIR = BASE_DIR / 'files'
FILE_PATH1 = FILES_DIR / 'file1.json'
FILE_PATH2 = FILES_DIR / 'file2.json'


@pytest.fixture
def json1():
    return load_json(FILE_PATH1)


@pytest.fixture
def json2():
    return load_json(FILE_PATH2)


def test_gendiff(json1, json2): 
    result = generate_diff(json1, json2)
    
    expected = [
        '{',
        '  - follow: False',
        '    host: hexlet.io',
        '  - proxy: 123.234.53.22',
        '  - timeout: 50',
        '  + timeout: 20',
        '  + verbose: True',
        '}',
    ]
    
    assert result.splitlines() == expected