# email-automation-with-python
This code shows you how to send automated email with
python, 
We use the smtp library to send the mail and the ssl library
for encryption, 
We start by imorting both library
import smtplib, ssl

To be able to send html content, we need import the 
MIMEText and MIMEMultipart
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

We instatiate the MIMEMultipart passing the argument 
alternative; this allow us to send both plain text and 
Html content

message = MIMEMultipart("alternative")
message["Subject"] = "Admission received"
message["From"] = sender
message["To"] = receiver

We mime the content and attach it to message to be sent
first_message = MIMEText(text, "plain")
second_message = MIMEText(html, "html")

message.attach(first_message)
message.attach(second_message)

We sent the email

port = 465
smtp_server = 'smtp.gmail.com'
context = ssl.create_default_context()
server = smtplib.SMTP_SSL(smtp_server, port, context=context)
#server.starttls(context=context)
server.login(sender, password)
server.sendmail(sender, receiver, message.as_string())
