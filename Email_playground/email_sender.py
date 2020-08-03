import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'Carlos Miau'
email['to'] = 'carlosayol@unisabana.edu.co'
email['subject'] = 'Holi miau, soy miau'

email.set_content(html.substitute({'name':'Padrecito Alonso'}),'html')

with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('carlosaolar@gmail.com','PERROS900M')
    smtp.send_message(email)
    print('NERV')