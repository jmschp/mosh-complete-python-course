# 15 Templates


from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import smtplib
from pathlib import Path
from string import Template # We need to import the "Template" class to replace the parameter in the template string


template = Template(Path(r"09 Python Standard Library\template.html").read_text()) # We are returning the content of the "template.html" as a string


message = MIMEMultipart() # first we create MIMEMultipart object. After we create the object we need to set the headers.
message["from"] = "Miguel"
message["to"] = "jmiguelpimenta@gmail.com"
message["subject"] = "Python email!"
email_body = template.substitute({"first_name": "Miguel", "last_name": "Pimenta"})  # We create the email body, and substitute the "$" parameter of the template with the ".substitute" method, using a dictonary or keuword arguments.
message.attach(MIMEText(email_body, "html"))
message.attach(MIMEImage(Path(r"C:\Users\jmigu\iCloudDrive\Os meus documentos\Documentos\Foto.jpg").read_bytes()))


with smtplib.SMTP(host="smtp.gmail.com", port=587) as smtp: #we need to create and open the SMTP and then close it. So it is better to use a "with" statment.
    smtp.ehlo() # This is a hello message to the smtp server. It's part of the smtp protcol
    smtp.starttls() # This puts the smtp connection in TLS mode.
    smtp.login("jmiguelpimenta@gmail.com", "jxnaeqluqkhhbeuc")
    smtp.send_message(message)
    print("Sent...")