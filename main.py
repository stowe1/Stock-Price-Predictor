import json
import os

import MetaTrader5

MetaTrader5.version()

def get_settings():
    with open('settings.json', 'r') as f:
        mt5_settings = json.load(f)
        f.close()
        print(mt5_settings)
    return mt5_settings

get_settings()

if __name__ == 'MetaTrader5':
    mt5_settings = get_settings()
    
    startup = mt5library.start_mt5(mt5_settings)
    print(startup)