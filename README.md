### Hexlet tests and linter status:
[![Actions Status](https://github.com/ESKolpakov/python-project-50/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/ESKolpakov/python-project-50/actions)
### CodeClimate
[![Maintainability](https://api.codeclimate.com/v1/badges/ba974e28575e2280e628/maintainability)](https://codeclimate.com/github/ESKolpakov/python-project-50/maintainability)
### GithubActions
[![Actions Status](https://github.com/ESKolpakov/python-project-50/actions/workflows/pyci.yml/badge.svg)](https://github.com/ESKolpakov/python-project-50/actions)

[![asciicast](https://asciinema.org/a/e56IWh6mm0km3Zn7dNJM09r4l.svg)](https://asciinema.org/a/e56IWh6mm0km3Zn7dNJM09r4l)


The general usage is (both absolute and relative paths to files are supported):

```bash
>> gendiff [-f file_format] file_path1 file_path2
```

Difference Generator provides help command as well:

```bash
>> gendiff --help

usage: gendiff [-h] [-f FORMAT] first_file second_file

Compares two configuration files and shows a difference.

positional arguments:
  first_file
  second_file

options:
  -h, --help            show this help message and exit
  -f FORMAT, --format FORMAT
                        set format of output (default: "stylish")
```