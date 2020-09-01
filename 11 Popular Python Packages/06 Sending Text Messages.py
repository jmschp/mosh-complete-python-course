# 06 Sending Text Messages

from twilio.rest import Client # This class represents a client to twilio Rest API

account_sid = "AC61b41543960b1719fafa3fb0a6a3201c"
auth_token = "ec9266ca025d0d0f918cc1192b177d0b"

client = Client(account_sid, auth_token)


client.messages.create(
    to = "+5511975520409",
    from_ = "+12058807590", 
    body = """
Olá,
Vocês está recebendo esta mensagem porque o Miguel te ama!
E neste momento ele está querendo um beijo!
\U0001f60e
"""
    )