import argparse

import json


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
    output_format = args.format
    
    print(args)
    
    file1 = json.load(open(f'gendiff/files/{first_file}'))
    file2 = json.load(open(f'gendiff/files/{second_file}'))
    
    print(file1)
    print(file2)

    
