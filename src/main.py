## Sends an SMS to the supplied number(s)
## This is mainly a personal project so I can easily implement SMS 
## notifications in my future projects.
#
## You will need to configure the program by entering your bulkgate.com 
## API key and wallet id into the .env dotfile
import os
import requests
from dotenv import load_dotenv

def send_sms(number, content, wallet=os.environ.get('WALLET')):
    load_env()


def load_env():
    """Initialise environment variables."""
    load_dotenv()
    app_id = os.environ.get('APP_ID')
    api_key = os.environ.get('API_KEY')
    wallet = os.environ.get('WALLET')

    

if __name__ == '__main__':
    run()
    print("Run successfully")