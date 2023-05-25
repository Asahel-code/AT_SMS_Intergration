import os
import africastalking
from dotenv import load_dotenv

load_dotenv()

# Initialize SDK
username = os.environ.get('AT_USERNAME')  
api_key = os.environ.get('AT_APIKEY')      
africastalking.initialize(username, api_key)


# Initialize a service e.g. SMS
sms = africastalking.SMS


#Use it asynchronously
def on_finish(error, response):
    if error is not None:
        raise error
    print(response)

sms.send("Hello Message!", ["+2547********"], callback=on_finish)