import MetaTrader5 as mt5Trader

def start_mt5(mt5_settings):

    username = mt5_settings['mt5']['username']
    password = mt5_settings['mt5']['password']
    server = mt5_settings['mt5']['server']
    mt5_path = mt5_settings['mt5']['path']
    
    mt5Trader_init = False
    try:
        mt5Trader_init = mt5Trader.initialize(
            username=username,
            password=password,
            server=server,
            mt5_path=mt5_path                               
        )
    
    except Exception as e:
        print(f"Error: {e}")
        mt5Trader_init = False