import os
import sys
import string

####################
# Help

def help ():
   print '''
	Usage: u [option]
	
	option:
		-caddisInstall    (Update installer on CDI1)
		-caddisClient     (Update installed client on HPGRMDS)
		-dia              (Update installer on FCDICAM)
		-ephoto           (Deploy service on CDI1)
		-turbo            (Update installer on CDI1)
		-hometurbo        (Update installer on PARENTS and MEDIAPC)
		-hometools        (Update tools on PARENTS and MEDIAPC)
		-tools            (Update installer on FCDICAM)
		-unload           (Update public folder)
		-web              (Update CDI1 web site)
		-psw              (Update MediaPC & Parents)
	''' 

####################
# Copy

def copy (f1, f2) :
	shutil.copy (f1,f2)


####################
# CopyMsi

def copyMsi (msiName) :
	os.system ('copy '+msiName+' \\\\mediapc\\public\\archive\\2005\\Tools')

####################
# CopyExe

def copyExe (exeName) :
	os.system ('copy '+exeName+' \\\\mediapc\\public\\Tools\\bin')


####################
# Different choices

if len (sys.argv)<2 :
	help()

elif sys.argv[1]=='-caddisInstall' :
	print 'Update the Caddis client installer' 
	os.chdir ("u:/code/CVS/Caddis/Install")
	os.system ('copy Release\* \\\\fcdicam\\click\\projects\\caddis\\Installer')
	
elif sys.argv[1]=='-caddisClient' :
	print 'Update the Caddis installed client on HPGRMDS' 
	os.chdir ("c:/Users/CVS/Caddis/src/bin")
	os.system ('copy Release\* "C:\\Program Files\\In Touch"')
	
elif sys.argv[1]=='-dia' :
	print 'Update the HP DIA installer on FCDICAM' 
	os.chdir ("U:/Code/shrek/install/HP DIA/Release")
	os.system ('copy *.msi \\\\fcdicam\\click\\projects\\Unloader\\Install')
	os.chdir ("U:/Code/shrek/install")
	os.system ('copy *.txt \\\\fcdicam\\click\\projects\\Unloader\\Install')

elif sys.argv[1]=='-ephoto' :
	print 'Copy EPhoto web service from local machine to CDI1' 
	os.chdir ("C:/Users/cvs/caddis/ephotoservice/bin")
	os.system ('xcopy .  \\\\cdi1\\large\\cdi1web\\ephotoservice\\bin  /S /I /Y')
	
elif sys.argv[1]=='-turbo' :
	print 'Update the Turbo Apps client installer' 
	os.chdir ("u:/code/TurboApps/Installer/Release")
	os.system ('copy "*.msi" "\\\\fcdicam\\click\\projects\\turboapps\\Installer"')

elif sys.argv[1]=='-tools' :
	print 'Update the HP DIA installer' 
	os.chdir ("U:/Code/HP Photo Tools/Install/MSI/Release")
	os.system ('copy * \\\\fcdicam\\click\\projects\\tools')

elif sys.argv[1]=='-hometools' :
	print 'Update tools on PARENTS and MEDIAPC' 
	os.chdir ("U:/Code/HP Photo Tools/Install/MSI/Release")
	copyMsi ('*.msi')

elif sys.argv[1]=='-psw' :
	print 'Put code into Parents and MediaPC' 
	os.chdir ('U:/Code/Exp/Microtronics/Microtronics Tools/Release')
	copyMsi ('*.msi')
	
elif sys.argv[1]=='-unload' :
	print 'Put code into public directory' 
	os.chdir ('c:/users/cvs/unloader/shared/bin')
	os.system ('copy *.* c:\\users\\archive\\public\\unload')
	
elif sys.argv[1]=='-web' :
	print 'Copy web site from local machine to CDI1' 
	os.chdir ("c:/users/web/cdi1")
	os.system ('xcopy '+sys.argv[2]+'  \\\\cdi1\\large\\cdi1web\\'+sys.argv[2]+'  /S /I /Y')
	
else :
	help()
