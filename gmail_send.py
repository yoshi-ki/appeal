# You can use this code if you write some texts in the main function!!

from apiclient.discovery import build #google api library
import base64
from email.mime.text import MIMEText
from oauth2client import file, client, tools
from httplib2 import Http


store = file.Storage('token.json')
creds = store.get()
if not creds or creds.invalid:
    flow = client.flow_from_clientsecrets('credentials.json', 'https://www.googleapis.com/auth/gmail.compose')
    #this url only allows sending, not reading
    #if you want to read you should use 'https://www.googleapis.com/auth/gmail.readonly' this scope.
    creds = tools.run_flow(flow, store)
service = build('gmail', 'v1', http=creds.authorize(Http()))


def create_message(sender, to, subject, message_text):
  """Create a message for an email.

  Args:
    sender: Email address of the sender.
    to: Email address of the receiver.
    subject: The subject of the email message.
    message_text: The text of the email message.

  Returns:
    An object containing a base64url encoded email object.
  """
  message = MIMEText(message_text)
  message['to'] = to
  message['from'] = sender
  message['subject'] = subject


  return {'raw': base64.urlsafe_b64encode(message.as_string().encode(encoding="UTF-8")).decode(encoding="UTF-8")}

def send_message(service, user_id, message):
  """Send an email message.

  Args:
    service: Authorized Gmail API service instance.
    user_id: User's email address. The special value "me"
    can be used to indicate the authenticated user.
    message: Message to be sent.

  Returns:
    Sent Message.
  """
  try:
    message = (service.users().messages().send(userId=user_id, body=message)
               .execute())
    print ('Message Id: %s' % message['id'])
    return message
  except :
    print ('An error occurred: %s' % error)

def main():
    #Please fill the information if you want to use this code
    message = create_message("write your email account","write the address you want to send email to ","write the title of this email","write the document")
    send_message(service,"me",message)
if __name__=='__main__':
    main()
