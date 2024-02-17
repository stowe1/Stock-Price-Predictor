import json
import os

def get_settings():
    with open('settings.json', 'r') as f:
        settings = json.load(f)
        print(settings)
    return settings

get_settings()