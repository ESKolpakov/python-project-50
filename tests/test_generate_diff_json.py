import pytest

from gendiff.generator import generate_diff


JSON_FILE1 = 'tests/fixtures/file1.json'
JSON_FILE2 = 'tests/fixtures/file2.json'
EXPECTED_JSON_RESULT = 'tests/fixtures/expected-json.txt'


def read_file(file_path):
    with open(file_path, 'r') as file:
        return file.read()
    

def test_generate_diff_json():
    expected_result = read_file(EXPECTED_JSON_RESULT)
    assert generate_diff(
        JSON_FILE1, JSON_FILE2, format='json'
        ) == expected_result
    