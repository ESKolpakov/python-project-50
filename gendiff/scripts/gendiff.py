#!/usr/bin/env python3

from gendiff.args_parser import parser_arg
from gendiff.generator import generate_diff
from gendiff.format.convert_files import convert_data_to_python


def main():
    file_path1, file_path2, format = parser_arg()
    print(generate_diff(file_path1, file_path2, format))


if __name__ == '__main__':
    main()
