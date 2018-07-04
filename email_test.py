import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
from email.MIMEBase import MIMEBase
from email import encoders

fromaddr = "nicholas.esterer@gmail.com"
toaddr = "n.alois.esterer@gmail.com"

msg = MIMEMultipart()

msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "sent from python buddang"

body = """

dirka dirka

asdlfkj


asd;lfkajsdf

"""

msg.attach(MIMEText(body, 'plain'))

filename = "./triangle.jpg"
attachment = open(filename, "rb")

part = MIMEBase('application', 'octet-stream')
part.set_payload((attachment).read())
encoders.encode_base64(part)
part.add_header('Content-Disposition', "attachment; filename= %s" %
       filename)

msg.attach(part)

server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "|{!n9Ph03n1x~4321")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
