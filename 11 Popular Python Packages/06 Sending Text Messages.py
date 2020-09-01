# 06 Sending Text Messages

from twilio.rest import Client # This class represents a client to twilio Rest API
import config

account_sid = config.twilio_account_sid
auth_token = config.twilio_auth_token

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