import argparse


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
    first_path = args.first_file
    second_path = args.second_file
    output_format = args.format
    
    return first_path, second_path, output_format