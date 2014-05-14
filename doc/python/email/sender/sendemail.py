import sys
from smtplib import SMTP

from_addr = 'seaman@comsystem.us'
to_addrs = ['mark.b.seaman@gmail.com']
msg = open('message.txt','r').read()

s = SMTP()
s.connect('smtp.webfaction.com')
s.login('seaman','mds959WF')
s.sendmail(from_addr, to_addrs, msg)
