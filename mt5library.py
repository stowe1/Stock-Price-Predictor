from MetaTrader5 import *
import MetaTrader5 as mt5
import traceback
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt



print("MetaTrader5 package author: ",mt5.__author__)
print("MetaTrader5 package version: ",mt5.__version__)

def start_mt5(mt5_settings):

    username = mt5_settings['mt5']['username']
    password = mt5_settings['mt5']['password']
    server = mt5_settings['mt5']['server']
    mt5_path = mt5_settings['mt5']['mt5_path']
    
    
    print(f"Username: {username}, Password: {password}, Server: {server}, Path: {mt5_path}")
    mt5_init = False
    try:
        mt5_init = mt5.initialize(path=mt5_path, login=username, password=password, server=server, timeout=1000, portable=False)
        print(f"MT5 initialized: {mt5_init}")
        print(traceback.format_exc())
    except Exception as e:
        print(f"Error: {e}")
        print(traceback.format_exc())
        mt5_init = False
    
    mt5_login = False
    if mt5_init:
        try:
            mt5_login = mt5.login(
                login=username,
                password=password,
                server=server
            )
            print(f"MT5 login: {mt5_login}")
        except Exception as e:
            print(f"Error: {e}")
            mt5_login = False
    
    if mt5_init and mt5_login:
        return True
    
 