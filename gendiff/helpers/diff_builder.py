COMMON = '  '
ADD = '+ '
REMOVE = '- '


def get_formated_keys(key):
    return {
        'common': f'{COMMON}{key}',
        'add': f'{ADD}{key}',
        'remove': f'{REMOVE}{key}'
    }


def get_common(keys):
    return keys['common']


def get_add(keys):
    return keys['add']


def get_remove(keys):
    return keys['remove']


def get_diff(dict1, dict2):
    result = {}
    sorted_keys = sorted(set(dict1) | set(dict2))
    for key in sorted_keys:
        format_keys = get_formated_keys(key)
        if key in dict1 and key in dict2:
            if dict1[key] == dict2[key]:
                result[get_common(format_keys)] = dict1[key]
            else:
                if (isinstance(dict1[key], dict)
                        and isinstance(dict2[key], dict)):
                    result[get_common(format_keys)] = \
                        get_diff(dict1[key], dict2[key])
                else:
                    result[get_remove(format_keys)] = dict1[key]
                    result[get_add(format_keys)] = dict2[key]
        elif key in dict1:
            result[get_remove(format_keys)] = dict1[key]
        else:
            result[get_add(format_keys)] = dict2[key]
    return result
