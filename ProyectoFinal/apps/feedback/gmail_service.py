from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
import base64
from email.mime.text import MIMEText

class GmailService:
    SCOPES = ['https://www.googleapis.com/auth/gmail.send']

    def __init__(self, client_secret_path):
        self.service = self.get_gmail_service(client_secret_path)

    def get_gmail_service(self, client_secret_path):
        flow = InstalledAppFlow.from_client_secrets_file(
            client_secret_path, self.SCOPES)
        credentials = flow.run_local_server(port=0)
        service = build('gmail', 'v1', credentials=credentials)
        return service

    def create_message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        return {'raw': base64.urlsafe_b64encode(message.as_bytes()).decode()}

    def send_message(self, user_id, message):
        try:
            message = (self.service.users().messages().send(userId=user_id, body=message)
                       .execute())
            print('Message Id: %s' % message['id'])
            return message
        except Exception as error:
            print('An error occurred: %s' % error)

# Uso de la clase
if __name__ == '__main__':
    gmail_service = GmailService("D:\Github\Credenciales\config.json")
    msg = gmail_service.create_message('m.e.b.d.0904@ifts18.edu.ar', 'm.e.b.d.0904@ifts18.edu.ar', 'Hello Gmail', 'Hello from Python!')
    gmail_service.send_message('me', msg)
