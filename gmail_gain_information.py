'''
    This code provides us the information of the email that is sent to someone in the march 2019.
    In order to run this, you should specify the date and address you sent.
'''
from apiclient.discovery import build #google api library
import base64
from email.mime.text import MIMEText
from oauth2client import file, client, tools
from httplib2 import Http

store = file.Storage('token.json')
creds = store.get()
"""
    if this code is not work, comment out the following code instead of the "if" scope
    flow = client.flow_from_clientsecrets('credentials.json', 'https://www.googleapis.com/auth/gmail.readonly')
    creds = tools.run_flow(flow, store)
"""
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', 'https://www.googleapis.com/auth/gmail.readonly')
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))

def GetMessage(service, user_id, DateFrom, DateTo, MessageTo):

  query = ''
  query += 'after:' + DateFrom + ' '
  query += 'before:' + DateTo + ' '
  query += 'To:' + MessageTo + ' '

  try:
    results = service.users().messages().list(userId=user_id,q=query).execute()
    message_ids = results.get('messages', [])
    message_list = []

    for ids in message_ids:
        id = ids.get('id')
        message = service.users().messages().get(userId=user_id, id=id).execute()
        if message['labelIds']==['SENT']:
            message_list.append(message['snippet'])
    return message_list
  except:
    print ('An error occurred: %s' % error)


def main():
    print(GetMessage(service,'me','2019-03-01','2019-03-31','You need to write the address you sent these to.'))

if __name__=='__main__':
    main()
