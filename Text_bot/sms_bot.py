from twilio.rest import Client

account_sid = 'ACa611a441477814f13e2679725b19bd60'
auth_token = '[AuthToken]'
client = Client(account_sid, auth_token)

message = client.messages.create(
    from_='+12029328726',
    to='+573005554985'
)

print(message.sid)