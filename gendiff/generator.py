import json


def generate_diff(file_path1, file_path2, format='stylish'):
    with open(file_path1) as f1, open(file_path2) as f2:
        file1_data = json.load(f1)
        file2_data = json.load(f2)
    keys = sorted(file1_data.keys() | file2_data.keys())
    lines = []
    for key in keys:
        if key not in file2_data:
            lines.append(f"- {key}: {file1_data[key]}")
        elif key not in file1_data:
            lines.append(f"+ {key}: {file2_data[key]}")
        elif file1_data[key] != file2_data[key]:
            lines.append(f"- {key}: {file1_data[key]}")
            lines.append(f"+ {key}: {file2_data[key]}")
        else:
            lines.append(f"  {key}: {file1_data[key]}")
    return "{\n" + "\n".join(lines) + "\n}"
