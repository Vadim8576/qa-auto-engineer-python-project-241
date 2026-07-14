
from gendiff.generate_diff import generate_diff
from gendiff.parser import parser


def main():
    data1, data2, output_format = parser()
    diff = generate_diff(data1, data2, output_format)

    print(diff)


if __name__ == "__main__":
    main()