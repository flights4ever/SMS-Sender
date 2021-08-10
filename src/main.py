## Sends an SMS to the supplied number(s)
## This is mainly a personal project so I can easily implement SMS 
## notifications in my future projects.
#
## You will need to configure the program by entering your bulkgate.com 
## API key and wallet id into the .env dotfile
import os
import requests
from dotenv import load_dotenv

def send_sms(number, content):
    app_id, api_key, wallet = load_env()
    url = 'https://portal.bulkgate.com/api/1.0/simple/transactional'

    
    
def load_env():
    """Initialise environment variables."""
    load_dotenv()
    app_id = os.environ.get('APP_ID')
    api_key = os.environ.get('API_KEY')
    wallet = os.environ.get('WALLET')

    return [app_id, api_key, wallet]


if __name__ == '__main__':
    send_sms(473190370, "Test")
    print("Run successfully")