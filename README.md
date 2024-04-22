### Hexlet tests and linter status, CodeClimate, Github Actions:
[![Actions Status](https://github.com/ESKolpakov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ESKolpakov/python-project-50/actions)
[![Maintainability](https://api.codeclimate.com/v1/badges/ba974e28575e2280e628/maintainability)](https://codeclimate.com/github/ESKolpakov/python-project-50/maintainability)
[![Python CI](https://github.com/ESKolpakov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/ESKolpakov/python-project-50/actions/workflows/pyci.yml)

[![asciicast](https://asciinema.org/a/e56IWh6mm0km3Zn7dNJM09r4l.svg)](https://asciinema.org/a/e56IWh6mm0km3Zn7dNJM09r4l)

For testing this project:
JSON:
```bash
gendiff tests/fixtures/file1.json tests/fixtures/file2.json
{
- follow: False
  host: hexlet.io
- proxy: 123.234.53.22
- timeout: 50
+ timeout: 20
+ verbose: True
}
```


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