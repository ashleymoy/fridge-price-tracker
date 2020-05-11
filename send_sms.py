import os
from dotenv import load_dotenv
from twilio.rest import Client

def send_sms():
    # get environment variables from .env
    load_dotenv()
    account_sid = os.environ.get('account_sid')
    auth_token = os.environ.get('auth_token')
    sender = os.environ.get('sender_number')
    recipient = os.environ.get('recipient_number')

    # create msg
    client = Client(account_sid, auth_token)
    message = client.messages.create( 
                              from_=sender,  
                              body='test',      
                              to=recipient 
                          )

    return message.sid