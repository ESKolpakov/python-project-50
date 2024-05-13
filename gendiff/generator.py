from gendiff.helpers.convert_data import convert_data
from gendiff.helpers.diff_builder import get_diff
from gendiff.helpers.get_format import get_format


def generate_diff(file_path1, file_path2, format='stylish'):
    data_format1 = file_path1.split('.')[-1]
    data_format2 = file_path2.split('.')[-1]
    dict1 = convert_data(file_path1, data_format1)
    dict2 = convert_data(file_path2, data_format2)
    diff = get_diff(dict1, dict2)
    return get_format(diff, format)
