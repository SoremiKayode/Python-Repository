import smtplib, ssl #smtplib gor sending the mail and ssl for encryption
from email.mime.text import MIMEText 
from email.mime.multipart import MIMEMultipart

# MIMEText and MIMEMultipart allow us to send both
# plain text and html content
sender = 'your sender email' #input your email
password = 'your receiver password' #input your password
receiver = 'your receiver email' #input the receeiver email

message = MIMEMultipart("alternative")
message["Subject"] = "Let's Help you build your Business"
# your email sunbject
message["From"] = sender
message["To"] = receiver

# Create the plain-text and HTML version of your message
text = """\
Hi,
How are you?
Real Python has many great tutorials:
www.realpython.com"""
html = """\
<html>
  <body>
  <div style="color:white; font-family:Garamond; background-image:url('https://img.freepik.com/free-vector/yellow-background-with-halftone-lines-design_1017-30148.jpg?size=626&ext=jpg'); background-size:cover; background-position:center; background-repeat:no-repeat;  text-align:center; padding:50px; ">
   <h1>Web Development</h1>
   <p style="font-style:italic;">Are you in need of a website. <br>
   We build flexible, scalable website<br>
       <a href="https://api.whatsapp.com/send?phone=2348179776605&text=Chat%20with%20me">Chat on whatsapp</a>
       
  </div>
   
  </body>
</html>
"""
first_message = MIMEText(text, "plain")
second_message = MIMEText(html, "html")

message.attach(first_message)
message.attach(second_message)

port = 465 # port to use in sendimg the mail, leave it as it is
smtp_server = 'smtp.gmail.com'
#smtp server it's always smtp. name of your email provider
# eg. smtp.mail.yahoo.com
context = ssl.create_default_context()
#instantiate the ssl encryption 
server = smtplib.SMTP_SSL(smtp_server, port, context=context)
#indtatiate the smtplib and pass the your email server,
# port and ssl encryption
server.login(sender, password)
# login in with your email and password
server.sendmail(sender, receiver, message.as_string())
# send the mail
