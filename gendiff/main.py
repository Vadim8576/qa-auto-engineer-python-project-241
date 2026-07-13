import argparse

from gendiff.generate_diff import generate_diff

from gendiff.load_json import load_json


def start():   
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        # choices=['plain', 'json'],
        default='plain',
        help='set format of output'
    )

    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    # output_format = args.format
    
    # print(args)
    
    file_path1 = f'gendiff/files/{first_file}'
    file_path2 = f'gendiff/files/{second_file}'
    
    
    json1 = load_json(file_path1)
    json2 = load_json(file_path2)
    
    diff = generate_diff(json1, json2)

    print(diff)
    

    
