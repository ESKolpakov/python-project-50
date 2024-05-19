from pathlib import Path
import requests
from gendiff.helpers.parser import parse


def read_file(file_path):
    path_to_file = Path(file_path)
    with open(path_to_file, 'r') as file:
        data = file.read()
    return data


def read_data_from_url(url):
    response = requests.get(url)
    response.raise_for_status()
    return response.text


def convert_data(file_path_or_url, data_format):
    if file_path_or_url.startswith('http://') \
            or file_path_or_url.startswith('https://'):
        data = read_data_from_url(file_path_or_url)
    else:
        data = read_file(file_path_or_url)
    return parse(data, data_format)
