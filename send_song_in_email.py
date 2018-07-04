import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os

env=os.environ

with open('./fromemail.txt','r') as f:
    fromaddr = f.read().strip()

toaddr = env['EMAIL_ADDRESS']

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "Your Recording"

with open('./emailmessage.txt','r') as f:
    body = f.read().format(NAME=env['NAME'],encoding="utf-8")

msg.attach(MIMEText(body, 'plain'))

filename = env['FILENAME']
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" %
       filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
with open('./fromemailpass.txt','r') as f:
    passwd=f.read()
    # Strip trailing new line. Not sure if this is consistent for all editors,
    # so we check if it is there first.
    if passwd[-1] == '\n':
        passwd=passwd[:-1]

server.login(fromaddr,passwd)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
