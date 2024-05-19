import os
from unittest.mock import patch
from gendiff.generator import generate_diff
from gendiff.helpers.convert_data import (
    read_file, read_data_from_url, convert_data
)
from gendiff.helpers.parser import parse


def get_fixture_path(file_name):
    current_dir = os.path.dirname(os.path.abspath(__file__))
    return os.path.join(current_dir, 'fixtures', file_name)


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def test_finding_different():
    json_path1 = get_fixture_path('file1.json')
    json_path2 = get_fixture_path('file2.json')
    yml_path1 = get_fixture_path('file1.yml')
    yml_path2 = get_fixture_path('file2.yml')

    result_stylish = read(get_fixture_path('expected-stylish.txt'))
    result_plain = read(get_fixture_path('expected-plain.txt'))
    result_json = read(get_fixture_path('expected-json.txt'))

    stylish_result_with_json = generate_diff(json_path1, json_path2)
    stylish_result_with_yml = generate_diff(yml_path1, yml_path2)
    plain_result_with_json = generate_diff(json_path1, json_path2, 'plain')
    plain_result_with_yml = generate_diff(yml_path1, yml_path2, 'plain')
    json_result_with_json = generate_diff(json_path1, json_path2, 'json')
    json_result_with_yml = generate_diff(yml_path1, yml_path2, 'json')

    assert stylish_result_with_json == result_stylish
    assert stylish_result_with_yml == result_stylish
    assert plain_result_with_json == result_plain
    assert plain_result_with_yml == result_plain
    assert json_result_with_json == result_json
    assert json_result_with_yml == result_json


@patch('requests.get')
def test_read_data_from_url(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = '{"key": "value"}'
    url = "https://something.com/json-data"
    data = read_data_from_url(url)
    assert data == '{"key": "value"}'


@patch('requests.get')
def test_convert_data_from_url(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = '{"key": "value"}'
    url = "https://something.com/json-data"
    data_format = 'json'
    parsed_data = convert_data(url, data_format)
    expected_data = {"key": "value"}
    assert parsed_data == expected_data


@patch('requests.get')
def test_parse_data_from_url(mock_get):
    mock_get.return_value.status_code = 200
    mock_get.return_value.text = """
    {
        "common": {
            "setting1": "Value 1",
            "setting2": 200,
            "setting3": true,
            "setting6": {
                "key": "value",
                "doge": {
                    "wow": ""
                }
            }
        },
        "group1": {
            "baz": "bas",
            "foo": "bar",
            "nest": {
                "key": "value"
            }
        },
        "group2": {
            "abc": 12345,
            "deep": {
                "id": 45
            }
        }
    }
    """
    url = "https://something.com/json-data"
    data_format = 'json'
    parsed_data = convert_data(url, data_format)
    expected_data = {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {'key': 'value', 'doge': {'wow': ''}}},
        'group1': {'baz': 'bas', 'foo': 'bar', 'nest': {'key': 'value'}},
        'group2': {'abc': 12345, 'deep': {'id': 45}}
    }
    assert parsed_data == expected_data


def test_read_file():
    file_path = get_fixture_path('file1.json')
    data = read_file(file_path)
    expected_data = read(file_path)
    assert data == expected_data


def test_parse():
    json_data = '{"key": "value"}'
    yaml_data = "key: value"
    parsed_json = parse(json_data, 'json')
    parsed_yaml = parse(yaml_data, 'yaml')
    assert parsed_json == {"key": "value"}
    assert parsed_yaml == {"key": "value"}


def test_convert_data():
    file_path_json = get_fixture_path('file1.json')
    file_path_yaml = get_fixture_path('file1.yml')
    parsed_json = convert_data(file_path_json, 'json')
    parsed_yaml = convert_data(file_path_yaml, 'yml')
    expected_data = {
        'common': {
            'setting1': 'Value 1',
            'setting2': 200,
            'setting3': True,
            'setting6': {
                'key': 'value',
                'doge': {
                    'wow': ''
                }
            }
        },
        'group1': {
            'baz': 'bas',
            'foo': 'bar',
            'nest': {
                'key': 'value'
            }
        },
        'group2': {
            'abc': 12345,
            'deep': {
                'id': 45
            }
        }
    }
    assert parsed_json == expected_data
    assert parsed_yaml == expected_data
