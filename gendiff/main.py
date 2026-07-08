import argparse


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
    
    print(args)

    
