
import pytest

from gendiff import generate_diff, loader
from gendiff.formatters import stylish

JSON_FILE1_NAME = 'json1.json'
JSON_FILE2_NAME = 'json2.json'
# BASE_DIR = Path(__file__).resolve().parent.parent
# FILES_DIR = BASE_DIR / 'files'
# FILE_PATH1 = FILES_DIR / 'file1.json'
# FILE_PATH2 = FILES_DIR / 'file2.json'


@pytest.fixture
def json1():
    return loader.load(JSON_FILE1_NAME)


@pytest.fixture
def json2():
    return loader.load(JSON_FILE2_NAME)


def test_generate_diff(json1, json2): 
    result = stylish.format(generate_diff.generate(json1, json2))
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


def test_identical_json(json1):
    result = stylish.format(generate_diff.generate(json1, json1))
    expected = [
        '{',
        '    follow: False',
        '    host: hexlet.io',
        '    proxy: 123.234.53.22',
        '    timeout: 50',
        '}',
    ]
    
    assert result.splitlines() == expected


def test_identical_json_keys_sorted(json1):
    result = stylish.format(generate_diff.generate(json1, json1))
    
    assert result.splitlines()[1].startswith('    follow')
    assert result.splitlines()[2].startswith('    host')
    assert result.splitlines()[3].startswith('    proxy')
    assert result.splitlines()[4].startswith('    timeout')


def test_diff_json_keys_sorted(json1, json2):
    result = stylish.format(generate_diff.generate(json1, json2))
    
    assert result.splitlines()[1].startswith('  - follow')
    assert result.splitlines()[2].startswith('    host')
    assert result.splitlines()[3].startswith('  - proxy')
    assert result.splitlines()[4].startswith('  - timeout')
    assert result.splitlines()[5].startswith('  + timeout')
    assert result.splitlines()[6].startswith('  + verbose')


def test_generate_diff_with_swapped_arguments(json1, json2):
    result = stylish.format(generate_diff.generate(json2, json1))
    
    expected = [
        '{',
        '  + follow: False',
        '    host: hexlet.io',
        '  + proxy: 123.234.53.22',
        '  - timeout: 20',
        '  + timeout: 50',
        '  - verbose: True',
        '}',
    ]
    
    assert result.splitlines() == expected

