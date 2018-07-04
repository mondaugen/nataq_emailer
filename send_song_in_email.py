import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders
import os

env=os.environ

fromaddr = env['FROM_EMAIL']
toaddr = env['EMAIL_ADDRESS']
emailmsgpath= env['EMAIL_MESSAGE']
emailpassword = env['EMAIL_PASSWORD']
emailsubject = env['EMAIL_SUBJECT']

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = emailsubject

with open(emailmsgpath,'r') as f:
    firstname=env['NAME'].split(' ')[0]
    body = f.read().format(NAME=firstname,encoding="utf-8")

msg.attach(MIMEText(body, 'plain'))

filename = env['FILENAME']
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" %
       os.path.basename(filename))

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()

server.login(fromaddr,emailpassword)
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
