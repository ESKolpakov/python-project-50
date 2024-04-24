from gendiff.format.bool_to_str import bool_to_str
from gendiff.format.data_parser import COMMON, ADD, REMOVE


def format_value(value):
    if isinstance(value, (dict, list, tuple, set)):
        return "[complex value]"
    elif isinstance(value, bool):
        return bool_to_str(value)
    elif isinstance(value, str):
        return f"'{value}'"
    else:
        return str(value)


def format_path(path):
    return '.'.join(path)


def format_message(action, path, value=None, next_value=None):
    formatted_path = format_path(path)
    if action == 'added':
        return f"Property '{formatted_path}' was added with value: {format_value(value)}"
    elif action == 'removed':
        return f"Property '{formatted_path}' was removed"
    elif action == 'updated':
        formatted_value = format_value(value)
        formatted_next_value = format_value(next_value)
        return f"Property '{formatted_path}' was updated. From {formatted_value} to {formatted_next_value}"


def plain(data):
    result = []


    def process_node(node, path=[]):
        for key, value in node.items():
            orig_key = key.lstrip(ADD).lstrip(REMOVE)
            current_path = path + [orig_key]
            if key.startswith(COMMON) and isinstance(value, dict):
                process_node(value, current_path)
            elif key.startswith(REMOVE) and f"{ADD}{orig_key}" in node:
                next_value = node[f"{ADD}{orig_key}"]
                result.append(format_message('updated', current_path, value, next_value))
            elif key.startswith(REMOVE):
                result.append(format_message('removed', current_path))
            elif key.startswith(ADD):
                result.append(format_message('added', current_path, value))
    process_node(data)
    return '\n'.join(result)
