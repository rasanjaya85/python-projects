#! /usr/local/bin/python3

import smtplib, ssl
from email import encoders
from email.mime.base import MIMEBase
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


smtp_server = 'smtp.gmail.com'
port = 587 # for starttls 
sender_email = 'rasanjaya1985@gmail.com'
receiver_email = 'rasaposha@gmail.com'

with open('password.txt', 'r') as f:
    password = f.read()

msg = MIMEMultipart("alternative")
msg["Subject"] = "Multipart Text"
msg["From"] = sender_email
msg["To"] = receiver_email

text = """
Hi There

This message is generated from Python. 
"""

html = """
<html>
    <body>
        <p> Hi, <br>
        How are you? <br>
        <a href="http://realpython.com"> Real Python </a> has many great tutorials.
        </p>
    </body>
</html>
"""

text = MIMEText(text, "plain")
html = MIMEText(html, "html")
filename = "coding.jpeg"

with open(filename, 'rb') as attachment:
    image = MIMEBase('application', 'octet-stream')
    image.set_payload(attachment.read())

encoders.encode_base64(image)
image.add_header("Content-Disposition", f"attachment; filename={filename}",)

msg.attach(text)
msg.attach(html)
msg.attach(image)

context = ssl.create_default_context()

try: 
    server = smtplib.SMTP(smtp_server, port)
    server.ehlo()
    server.starttls(context=context)
    server.ehlo()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    # email body
except Exception as e:
    print(e)

finally:
    server.quit()