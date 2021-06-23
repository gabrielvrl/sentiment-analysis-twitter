import configparser

def config_api():
    config = configparser.ConfigParser()

    config.read('config.ini')
    consumer_key = config['auth']['consumer_key']
    consumer_secret = config['auth']['consumer_secret']
    access_token = config['auth']['access_token']
    access_token_secret = config['auth']['access_token_secret']

    return(consumer_key,consumer_secret,access_token,access_token_secret)

consumer_key,consumer_secret,access_token,access_token_secret = config_api()