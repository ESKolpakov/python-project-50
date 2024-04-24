from gendiff.format.bool_to_str import bool_to_str
from gendiff.format.data_parser import COMMON, ADD, REMOVE


def format_key_value(key, value, indent, is_nested=False):
    if not is_nested:
        return f"{indent}{key}: {value}"
    return f"{indent}{key}: {{\n{value}\n{indent}}}"


def stylish(data, replacer=' ', spaces_count=4):
    def dict_to_str(data, depth):
        lines = []
        indent = replacer * spaces_count * depth
        inner_indent = replacer * spaces_count * (depth + 1)
        for key, value in data.items():
            if isinstance(value, dict):
                nested = dict_to_str(value, depth + 1)
                line = format_key_value(key, nested, inner_indent, is_nested=True)
            else:
                formatted_value = bool_to_str(value)
                line = format_key_value(key, formatted_value, inner_indent)
            lines.append(line)
        result = '\n'.join(lines)
        if depth == 1:
            return f"{{\n{result}\n}}"
        return result
    return dict_to_str(data, 0)
