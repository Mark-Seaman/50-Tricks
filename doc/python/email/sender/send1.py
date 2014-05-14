
import smtplib
from email.mime.text import MIMEText

textfile='message.txt'
fp = open(textfile, 'rb')
msg = MIMEText(fp.read())
fp.close()

msg['Subject'] = 'The contents of %s' % textfile
from_addr = 'seaman@comsystem.us'
to_addrs = ['mark.b.seaman@gmail.com']
msg['From'] = from_addr
msg['To'] = to_addrs[0]

s = smtplib.SMTP('smtp.webfaction.com')
s.login('seaman','mds959WF')
s.sendmail(from_addr, to_addrs, msg.as_string())
s.quit()
