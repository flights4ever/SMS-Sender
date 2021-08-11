## Sends an SMS to the supplied number(s)
## This is mainly a personal project so I can easily implement SMS 
## notifications in my future projects.
#
## You will need to configure the program by entering your bulkgate.com 
## API key and wallet id into the .env dotfile
import os
import requests
import json
from dotenv import load_dotenv

app_id, api_key, wallet = load_env()

def send_sms(number, country, content="Test", sender_id="gText", sender_id_value="SMS-Sender"):
    url = 'https://portal.bulkgate.com/api/1.0/simple/transactional'

    request = {
        "application_id": app_id, 
        "application_token": api_key, 
        "number": number, 
        "text": content, 
        "unicode": True,
        "sender_id": sender_id,
        "sender_id_value": sender_id_value,
        "country": country
    }
    return json.loads(requests.post(url, json=request).text)
    

def get_credits(app_id, api_key):
    response = json.loads(requests.get('https://portal.bulkgate.com/api/1.0/simple/info', params={'application_id':app_id, 'application_token':api_key}).text)
    print(response)
    try:
        if response['data']:
            return response['data']['credit']
    except KeyError:
        if response['error']:
            get_credits(app_id, api_key)
        else:
            raise Exception(f'get_credits() had a stroke {response}')


    
def load_env():
    """Initialise environment variables."""
    load_dotenv()
    app_id = os.environ.get('APP_ID')
    api_key = os.environ.get('API_KEY')
    wallet = os.environ.get('WALLET')

    return [app_id, api_key, wallet]
