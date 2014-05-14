#!/usr/bin/env python

import sys

output = open('/home/seaman/mail.txt', 'a')
output.write(sys.stdin.read())
output.close()
