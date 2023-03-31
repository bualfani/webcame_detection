import imghdr
import smtplib
from email.message import EmailMessage

# add google password received from generating one
password = "your_password"

def send_email(img_path):
    email_message = EmailMessage
    email_message['Subject'] = 'New Customer'
    email_message.set_content('Hey, a new customer is here')

    with open(img_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))


