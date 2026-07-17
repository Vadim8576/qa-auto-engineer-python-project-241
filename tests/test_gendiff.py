
from pathlib import Path

import pytest

from gendiff import loader
from gendiff.generate_diff import generate_diff

BASE_DIR = Path(__file__).resolve().parent.parent
FILES_DIR = BASE_DIR / 'tests' / 'test_data'

TEST_CASES = [
    (FILES_DIR / "json1.json", FILES_DIR / "json2.json"),
    (FILES_DIR / "yml1.yml", FILES_DIR / "yml2.yml"),
]


# tests stylish out

@pytest.mark.parametrize("path1,path2", TEST_CASES, ids=["json", "yaml"])
def test_different_files_stylish_out(path1, path2): 
    data1 = loader.load(str(path1))
    data2 = loader.load(str(path2))
    result = generate_diff(data1, data2)
    expected = [
        '{',
        '  - follow: false',
        '    host: hexlet.io',
        '  - proxy: 123.234.53.22',
        '  - timeout: 50',
        '  + timeout: 20',
        '  + verbose: true',
        '}',
    ]
    
    assert result.splitlines() == expected


@pytest.mark.parametrize("path1,_", TEST_CASES, ids=["json", "yaml"])
def test_identical_files_stylish_out(path1, _):
    data = loader.load(str(path1))
    result = generate_diff(data, data)
    expected = [
        '{',
        '    follow: false',
        '    host: hexlet.io',
        '    proxy: 123.234.53.22',
        '    timeout: 50',
        '}',
    ]
    
    assert result.splitlines() == expected


@pytest.mark.parametrize("path1,path2", TEST_CASES, ids=["json", "yaml"])
def test_keys_sorted_stylish_out(path1, path2):
    data1 = loader.load(str(path1))
    data2 = loader.load(str(path2))
    result = generate_diff(data1, data2)
    
    assert result.splitlines()[1].startswith('  - follow')
    assert result.splitlines()[2].startswith('    host')
    assert result.splitlines()[3].startswith('  - proxy')
    assert result.splitlines()[4].startswith('  - timeout')
    assert result.splitlines()[5].startswith('  + timeout')
    assert result.splitlines()[6].startswith('  + verbose')
    

@pytest.mark.parametrize("path1,path2", TEST_CASES, ids=["json", "yaml"])
def test_generate_diff_with_swapped_arguments_stylish_out(path1, path2):
    data1 = loader.load(str(path1))
    data2 = loader.load(str(path2))
    result = generate_diff(data2, data1)
    
    expected = [
        '{',
        '  + follow: false',
        '    host: hexlet.io',
        '  + proxy: 123.234.53.22',
        '  - timeout: 20',
        '  + timeout: 50',
        '  - verbose: true',
        '}',
    ]
    
    assert result.splitlines() == expected


# tests plain out

@pytest.mark.parametrize("path1,path2", TEST_CASES, ids=["json", "yaml"])
def test_different_files_plain_out(path1, path2): 
    data1 = loader.load(str(path1))
    data2 = loader.load(str(path2))
    result = generate_diff(data1, data2, 'plain')
    expected = [
        "Property 'follow' was removed",
        "Property 'proxy' was removed",
        "Property 'timeout' was updated. From 50 to 20",
        "Property 'verbose' was added with value: true",
    ]
    
    assert result.splitlines() == expected


@pytest.mark.parametrize("path1,_", TEST_CASES, ids=["json", "yaml"])
def test_identical_files_plain_out(path1, _):
    data = loader.load(str(path1))
    result = generate_diff(data, data, 'plain')
    expected = ''
    
    assert result == expected