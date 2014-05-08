import os
import sys
import string

####################
# Directories
dir1 = "C:\\Program Files\\Hewlett-Packard\\PhotoSmart\\Photo Imaging\\Unload"
dir2 = "c:\\cvs\\stooges\\shared\\debug"
dir3 = "c:\\cvs\\stooges\\shared\\release"

####################
# Help

def help ():
   print '''
	Usage: g [option]
	
	option:
		-kiosk
		-tools
		-tron
		-croft
		-frogger
		-shrek
		-caddis
		-web
		-integrate
		-issues
		-lancam
		-ephoto
		-ephoto2
	''' 

####################
# Archive code

def archive (project):
	os.chdir ("u:/code")
	os.system ('u:')
	os.system ('cclean '+project)

	os.system ('zip '+project)
	os.system ('rm -rf '+project)



####################
# Get common code

def getCommonCode (project):
	os.system ('mkdir '+project+'\shared\common')
	os.system ('get   cue-components/SharedBin '+project+'\shared\common\SharedBin ')
	os.system ('get   cue-components/SharedInc '+project+'\shared\common\SharedInc')
	os.system ('get   cue-components/SharedLib '+project+'\shared\common\SharedLib')



####################
# Get Unloader code

def getUnloaderCode (project):
	os.system ('get cue-components/src/Unloader '+project) 

	os.system ('mkdir '+project+'\shared\Skins')
	os.system ('mkdir '+project+'\shared\Skins\hp1')
	os.system ('get  cue-ui/src/Skins/hp1/ul '+project+'\shared\Skins\hp1\ul')
	os.system ('get  cue-ui/src/Skins/hp1/bc '+project+'\shared\Skins\hp1\bc')
	os.system ('get  cue-components/src/Unloader/shared/BBFE/unload/loc/enu	'+project+'\shared\Skins\hp1\ul\loc')



####################
# Different choices

if len (sys.argv)<2 :
	help()


elif sys.argv[1]=='-kiosk' :
	print 'Get KIOSK code from CVS' 
	archive('kiosk')
	os.system ('get photosmart/pc-kiosk kiosk') 
	os.system ('p -net')
	os.system ('devenv kiosk.sln /build Debug')

elif sys.argv[1]=='-croft' :
	print 'Get code from CVS' 
	archive('croft')
	getUnloaderCode('croft')
	getCommonCode('croft')


elif sys.argv[1]=='-tron' :
	print 'Get code from CVS' 
	archive('tron')
	getUnloaderCode('tron')
	getCommonCode('tron')


elif sys.argv[1]=='-frogger' :
	print 'Get code from CVS' 
	archive('frogger')
	getUnloaderCode('frogger')
	getCommonCode('frogger')


elif sys.argv[1]=='-shrek' :
	print 'Get code from CVS' 
	archive('shrek')
	getUnloaderCode('shrek')
	getCommonCode('shrek')


elif sys.argv[1]=='-caddis' :
	print 'Get the Caddis client source from CVS' 
	os.chdir ("u:/code")
	os.system ('u:')
	os.system ('cclean caddis')
	os.system ('rm -rf caddis/test')
	os.system ('zip caddis')
	os.system ('rm -rf caddis')
	#os.system ('get-caddis')

elif sys.argv[1]=='-tools' :
	print 'Get hputilities code from CVS' 
	os.system ('u:')
	os.chdir  ("u:/code")
	os.system ('cclean "HP Photo Tools"')
	os.system ('zip "HP Photo Tools"')
	os.system ('rm -rf hpphot~1')
	os.system ('get "hputilities/HP Photo Tools" "HP Photo Tools"')


elif sys.argv[1]=='-web' :
	print 'Copy web site from local machine to CDI1' 
	os.chdir ("c:/users/web/cdi1")
	os.system ('xcopy '+sys.argv[2]+'  \\\\cdi1\\large\\cdi1web\\'+sys.argv[2]+'  /S /I /Y')
	

elif sys.argv[1]=='-integrate' :
	print 'Copy integrate web page from local machine to CDI1' 
	os.chdir ("C:/Inetpub/wwwroot/integrate")
	os.system ('copy integrate.aspx  \\\\cdi1\\large\\cdi1web\\integrate')
	os.system ('copy bin\\integrate.dll  \\\\cdi1\\large\\cdi1web\\integrate\\bin')
	

elif sys.argv[1]=='-issues' :
	print 'Copy integrate web page from local machine to CDI1' 
	os.chdir ("C:/Inetpub/wwwroot/issues")
	os.system ('copy issues.aspx  \\\\cdi1\\large\\cdi1web\\issues')
	os.system ('copy bin\\issues.dll  \\\\cdi1\\large\\cdi1web\\issues\\bin')
	

elif sys.argv[1]=='-lancam' :
	print 'Copy LanCam web service from local machine to CDI1' 
	os.chdir ("c:/inetpub/wwwroot/mpvservice/bin")
	os.system ('xcopy .  \\\\cdi1\\large\\cdi1web\\mpvservice\\bin  /S /I /Y')
	

elif sys.argv[1]=='-ephoto2' :
	print 'Copy EPhoto web service from local machine to CDI1' 
	os.chdir ("c:/inetpub/wwwroot/ephotoservice/bin")
	os.system ('xcopy .  \\\\cdi1\\large\\cdi1web\\ephotoservice\\bin  /S /I /Y')

	
elif sys.argv[1]=='-ephoto' :
	print 'Copy EPhoto web service from local machine to HPGRCONN10' 
	os.chdir ("c:/users/code/net/ephotoservice/bin")
	os.system ('xcopy .  \\\\hpgrconn10\\c\\inetpub\\wwwroot\\ephotoservice\\bin  /S /I /Y')
	os.chdir ("C:\\Users\\Cue\\turbo-apps\\TAMonitor\\bin\\Release")
	os.system ('copy TAMonitor.exe \\\\hpgrconn10\\c\\users\\lancam\\TAMonitor')

	
	
else :
	help()
