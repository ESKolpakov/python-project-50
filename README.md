### Hexlet tests and linter status, CodeClimate, Github Actions:
[![Actions Status](https://github.com/ESKolpakov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ESKolpakov/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ba974e28575e2280e628/maintainability)](https://codeclimate.com/github/ESKolpakov/python-project-50/maintainability)
[![Python CI](https://github.com/ESKolpakov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/ESKolpakov/python-project-50/actions/workflows/pyci.yml)

Asciinema:
[![asciicast](https://asciinema.org/a/ZPbygaTaHtcHVCIjTAwEDWfyu.svg)](https://asciinema.org/a/ZPbygaTaHtcHVCIjTAwEDWfyu)


```bash
>> gendiff --help
usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file            first config file
  second_file           second config file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output
```
To compare the two test files attached to the project, enter one of these commands:
```bash
>> gendiff tests/fixtures/file1.yml tests/fixtures/file2.yml
>> gendiff -f stylish tests/fixtures/file1.json tests/fixtures/file2.json
>> gendiff -f plain tests/fixtures/file1.json tests/fixtures/file2.json
>> gendiff -f json tests/fixtures/file1.json tests/fixtures/file2.json
```
