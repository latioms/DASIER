
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = 'ACd318a27d607a50e86459dbd761d32a96'
auth_token = 'd1cbe41a50697928d0d21787844eeb10'
client = Client(account_sid, auth_token)

message = client.messages \
                .create(
                     body="Join Earth's mightiest heroes. Like Kevin Bacon.",
                     from_='+15073535937',
                     to='+237699875974', 
                     
                 )

print(message.sid)