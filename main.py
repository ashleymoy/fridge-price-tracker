from classes import Fridge
import os
from dotenv import load_dotenv

load_dotenv() # load env variables 

def send_text():
    # get environment variables
    acct_id = os.getenv('account_sid')
    auth_token = os.environ.get('auth_token')
    print(acct_id)

if __name__ == "__main__":
    send_text()
    # samsung = Fridge('Samsung','RF23R6201WW')
    # print(samsung.check_home_depot())
