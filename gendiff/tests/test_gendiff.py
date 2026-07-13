import pytest

from gendiff.generate_diff import generate_diff

from gendiff.load_json import load_json



# @pytest.fixture
# def json1():
#     return load_json(file_path1)


# @pytest.fixture
# def json1():
#     return load_json(file_path1)


# @pytest.fixture
# def json1():
#     return tmp_json_file({"a": 1, "b": 2})



def test_gendiff():
    
    file_path1 = f'gendiff/files/file1.json'
    file_path2 = f'gendiff/files/file2.json'
    
    json1 = load_json(file_path1)
    json2 = load_json(file_path2)
    
    result = generate_diff(json1, json2)
    
    expected = (
        '{\n'
        '  - follow: False\n'
        '    host: hexlet.io\n'
        '  - proxy: 123.234.53.22\n'
        '  - timeout: 50\n'
        '  + timeout: 20\n'
        '  + verbose: True\n'
        '}'
    )
    
    assert result == expected