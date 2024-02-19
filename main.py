import json
import os

import mt5library



def get_settings():
    with open('settings.json', 'r') as f:
        mt5_settings = json.load(f)
        f.close()
        print(mt5_settings)
    return mt5_settings


if __name__ == '__main__':
    mt5_settings = get_settings()
    
    startup = mt5library.start_mt5(mt5_settings)
    print(startup)