import imghdr
import smtplib
from email.message import EmailMessage

# add google password received from generating one
PASSWORD = "your_password"
SENDER = 'your_email'
RECEIVER = 'your_email'

def send_email(img_path):
    email_message = EmailMessage
    email_message['Subject'] = 'New Customer'
    email_message.set_content('Hey, a new customer is here')

    with open(img_path, 'rb') as file:
        content = file.read()
    email_message.add_attachment(content, maintype='image', subtype=imghdr.what(None, content))

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(SENDER, PASSWORD)
    gmail.sendmail(SENDER, RECEIVER, email_message.as_string())
    gmail.quit()

if __name__ == '__main__':
    send_email(img_path='image/19.png')
