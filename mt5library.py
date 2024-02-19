import MetaTrader5



def start_mt5(mt5_settings):

    username = mt5_settings['mt5']['username']
    password = mt5_settings['mt5']['password']
    server = mt5_settings['mt5']['server']
    mt5_path = mt5_settings['mt5']['mt5_path']
    
    mt5_init = False
    try:
        mt5_init = MetaTrader5.initialize(
            login=username,
            password=password,
            server=server,
            path=mt5_path                               
        )
        print(f"MT5 initialized: {mt5_init}")
    
    except Exception as e:
        print(f"Error: {e}")
        mt5_init = False
    
    mt5_login = False
    if mt5_init:
        try:
            mt5_login = MetaTrader5.login(
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