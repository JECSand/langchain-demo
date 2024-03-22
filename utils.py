import json
import os.path


# Get project configurations=
def get_configs():
    if os.path.isfile('config.json'):
        with open('config.json', 'r') as f:
            return json.load(f)
    raise FileNotFoundError
