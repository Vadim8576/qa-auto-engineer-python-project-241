
from gendiff.generate_diff import generate_diff
from gendiff.parser import parser


def main():
    first_path, second_path, output_format = parser()
    diff = generate_diff(first_path, second_path, output_format)

    print(diff)


if __name__ == "__main__":
    main()