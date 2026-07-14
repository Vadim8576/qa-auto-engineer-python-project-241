
# from pathlib import Path

# import pytest

# from gendiff import loader
# from gendiff.generate_diff import generate_diff

# BASE_DIR = Path(__file__).resolve().parent.parent
# FILES_DIR = BASE_DIR / 'tests' / 'test_data'

# TEST_CASES = [
#     (FILES_DIR / 'json1.json', FILES_DIR / 'json2.json'),
#     (FILES_DIR / 'yml1.yml', FILES_DIR / 'yml2.yml'),
# ]


# @pytest.mark.parametrize('path1,path2', TEST_CASES, ids=['json', 'yaml'])
# def test_generate_diff(path1, path2): 
#     data1 = loader.load(str(path1))
#     data2 = loader.load(str(path2))
#     result = generate_diff(data1, data2)
#     expected = [
#         '{',
#         '  - follow: false',
#         '    host: hexlet.io',
#         '  - proxy: 123.234.53.22',
#         '  - timeout: 50',
#         '  + timeout: 20',
#         '  + verbose: true',
#         '}',
#     ]
    
#     assert result.splitlines() == expected


# @pytest.mark.parametrize('path1,_', TEST_CASES, ids=['json', 'yaml'])
# def test_identical_files(path1, _):
#     data = loader.load(str(path1))
#     result = generate_diff(data, data)
#     expected = [
#         '{',
#         '    follow: false',
#         '    host: hexlet.io',
#         '    proxy: 123.234.53.22',
#         '    timeout: 50',
#         '}',
#     ]
    
#     assert result.splitlines() == expected


# @pytest.mark.parametrize('path1,path2', TEST_CASES, ids=['json', 'yaml'])
# def test_keys_sorted(path1, path2):
#     data1 = loader.load(str(path1))
#     data2 = loader.load(str(path2))
#     result = generate_diff(data1, data2)
    
#     assert result.splitlines()[1].startswith('  - follow')
#     assert result.splitlines()[2].startswith('    host')
#     assert result.splitlines()[3].startswith('  - proxy')
#     assert result.splitlines()[4].startswith('  - timeout')
#     assert result.splitlines()[5].startswith('  + timeout')
#     assert result.splitlines()[6].startswith('  + verbose')
    

# @pytest.mark.parametrize('path1,path2', TEST_CASES, ids=['json', 'yaml'])
# def test_generate_diff_with_swapped_arguments(path1, path2):
#     data1 = loader.load(str(path1))
#     data2 = loader.load(str(path2))
#     result = generate_diff(data2, data1)
    
#     expected = [
#         '{',
#         '  + follow: false',
#         '    host: hexlet.io',
#         '  + proxy: 123.234.53.22',
#         '  - timeout: 20',
#         '  + timeout: 50',
#         '  - verbose: true',
#         '}',
#     ]
    
#     assert result.splitlines() == expected

