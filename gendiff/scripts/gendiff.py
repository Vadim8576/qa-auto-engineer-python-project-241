
import argparse

from gendiff import generate_diff

from gendiff import loader



def main():
    parser = argparse.ArgumentParser(
        prog='gendiff',
        description='Compares two configuration files and shows a difference.',
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument('first_file')
    parser.add_argument('second_file')
    parser.add_argument(
        '-f', '--format',
        choices=['stylish', 'json'],
        default='stylish',
        help='set format of output'
    )

    args = parser.parse_args()
    first_file = args.first_file
    second_file = args.second_file
    # output_format = args.format
    
    print(args)

    
    
    
    data1 = loader.load(first_file)
    data2 = loader.load(second_file)
    
    diff = generate_diff.generate(data1, data2)

    print(diff)


if __name__ == "__main__":
    main()