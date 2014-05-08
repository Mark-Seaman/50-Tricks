#!/usr/bin/env python 
# Convert the character encoding

text = open('text-sample').read().decode('ascii', 'ignore')
print text
