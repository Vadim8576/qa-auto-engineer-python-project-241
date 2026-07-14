
from gendiff import generate_diff, parser
from gendiff.formatters import stylish


def main():
    data1, data2 = parser.parser()
    diff = generate_diff.generate(data1, data2)

    print(stylish.format(diff))


if __name__ == "__main__":
    main()