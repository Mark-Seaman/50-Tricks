import os
import sys
import string

####################
# Help

def help ():
   print '''
	Usage: o [option]
	
	option:
		-clear    
		-edit     
		-view
	''' 

####################
# Different choices

os.chdir ("C:/Documents and Settings/seaman/Local Settings/Temp")
word = '"c:/Program files/windows nt/accessories/wordpad.exe"'

if len (sys.argv)<2 :
	help()

elif sys.argv[1]=='-clear' :
	os.system ('del options.xml')
	
elif sys.argv[1]=='-edit' :
	os.system (word+' options.xml')
	
elif sys.argv[1]=='-view' :
	os.system ('options.xml')
	
else :
	help()
