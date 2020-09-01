# 14 Sending Emails

from email.mime.multipart import MIMEMultipart
# In python we have a package "email" with a sub packge "mime" that stands for multipurpose internet mail extensions.
# This a is a standard that define the format for email messages.
# The "MIMEMultipart"class allows as to send an email message that inclueds both html and plain text content.


from email.mime.text import MIMEText # Here import the "MIMEText" class. To attach a text or html to our email
from email.mime.image import MIMEImage # Here import the "MIMEImage" class. To attach a images to our email.We need to pass it as binary.

import smtplib # Importing the "smtplib" module to creat an smtp server.

from pathlib import Path



message = MIMEMultipart() # first we create MIMEMultipart object. After we create the object we need to set the headers.
message["from"] = "Miguel"
message["to"] = "jmiguelpimenta@gmail.com"
message["subject"] = "Python email!"
message.attach(MIMEText("Email enviado pelo python"))
message.attach(MIMEImage(Path(r"C:\Users\jmigu\iCloudDrive\Os meus documentos\Documentos\Foto.jpg").read_bytes()))

with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp: #we need to create and open the SMTP and then close it. So it is better to use a "with" statment.
    smtp.ehlo() # This is a hello message to the smtp server. It's part of the smtp protcol
    smtp.starttls() # This puts the smtp connection in TLS mode.
    smtp.login("jmiguelpimenta@gmail.com", "jxnaeqluqkhhbeuc")
    smtp.send_message(message)
    print("Sent...")