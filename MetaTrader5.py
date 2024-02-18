import json
import os

def get_settings():
    with open('settings.json', 'r') as f:
        mt5_settings = json.load(f)
        f.close()
        print(mt5_settings)
    return mt5_settings

get_settings()