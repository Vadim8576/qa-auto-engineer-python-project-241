import argparse

from gendiff import loader


def parser():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        choices=['stylish', 'plain', 'json'],
        default='stylish',
        help='set format of output'
    )

    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    output_format = args.format
    
    data1 = loader.load(first_file)
    data2 = loader.load(second_file)
    
    return data1, data2, output_format