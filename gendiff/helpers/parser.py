import json
import yaml


def parse(data, data_format):
    if data_format == 'json':
        return json.loads(data)
    elif data_format in ['yaml', 'yml']:
        return yaml.safe_load(data)
    else:
        raise ValueError(f"Unsupported format: {data_format}")
