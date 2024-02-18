import MetaTrader5



def start_mt5(mt5_settings):

    username = mt5_settings['mt5']['username']
    password = mt5_settings['mt5']['password']
    server = mt5_settings['mt5']['server']
    mt5_path = mt5_settings['mt5']['mt5_path']
    
    MetaTrader5_init = False
    try:
        MetaTrader5_init = MetaTrader5.initizale(
            username=username,
            password=password,
            server=server,
            mt5_path=mt5_path                               
        )
        print(f"MT5 initialized: {MetaTrader5_init}")
    
    except Exception as e:
        print(f"Error: {e}")
        MetaTrader5_init = False
    
    if MetaTrader5_init:
        print("MT5 initialized successfully")
        return True
    else:
        print("MT5 initialization failed")
        return False