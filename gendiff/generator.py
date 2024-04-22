from gendiff.format.convert_files import convert_data_to_python
from gendiff.format.data_parser import get_diff
from gendiff.format.get_format import get_format


def generate_diff(file_path1, file_path2, format='stylish'):
    dict1 = convert_data_to_python(file_path1)
    dict2 = convert_data_to_python(file_path2)
    diff = get_diff(dict1, dict2)

    return get_format(diff, format)
