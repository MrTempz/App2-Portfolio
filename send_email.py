import smtplib
import ssl
from email_credentials import username, password, receiver

def send_email(message):

    host = 'smtp.gmail.com'
    port = 465



    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)
