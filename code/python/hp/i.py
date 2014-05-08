import os
import sys
import string

####################
# Help

def help ():
   print '''
	Usage: i [option]
	
	option:
		-caddis    
		-dia             
		-turbo            
		-tools            
	''' 


####################
# Different choices

if len (sys.argv)<2 :
	help()

elif sys.argv[1]=='-caddis' :
	print 'Install Caddis client'
	os.system ('U:\\Code\\CVS\\Caddis\\install\\Release\\caddis.msi')
	
	
elif sys.argv[1]=='-dia' :
	print 'Update the HP PhotoTools client installer' 
	os.system ('U:')
	os.chdir ("U:/Code/shrek/install/HP DIA/Release")
	os.system ('"HP DIA.msi"')
	
elif sys.argv[1]=='-psw' :
	print 'Update the Micronics Tools ' 
	os.system ('"U:\\Code\\Exp\\Microtronics\\Microtronics Tools\\Release\\Microtronics Tools.msi"')
	
	
elif sys.argv[1]=='-turbo' :
	print 'Update the Turbo Apps client installer' 
	os.system ('U:')
	os.system ('"U:\\Code\\TurboApps\\installer\\Release\\HP Turbo Apps.msi"')


elif sys.argv[1]=='-tools' :
	print 'Update the HP PhotoTools installer' 
	os.system ('"U:\\Code\\HP Photo Tools\\Install\\MSI\\Release\\HP Photo Tools.msi"')

else :
	help()
