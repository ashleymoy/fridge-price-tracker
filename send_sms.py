import os
from dotenv import load_dotenv
from twilio.rest import Client

def send_sms():
    # get environment variables from .env
    load_dotenv()
    sender = os.environ.get('sender_number')
    recipient = os.environ.get('recipient_number')

    # create msg
    message = Client.messages.create( 
                              from_=sender,  
                              body='This is a test.',      
                              to=recipient 
                          ) 
    print(message.sid)