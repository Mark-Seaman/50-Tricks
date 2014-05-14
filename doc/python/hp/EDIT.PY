import os
import sys
import win32api

####################
# Help

def help ():
	print '''
		usage: e [option]

		option:
			-cw  [file]     (CodeWright)
			-n   [file]     (Notepad)
			-w   [file]     (Word)
			-vs  [file]     (Visual Studio)
			-r   [file]    	(Ruby editor)
			
			-user          	(User ID)
			-unload	       	(Zelda Unloader)
			-caddis        	(Caddis client software)
 			-ephoto        	(Deploy service on CDI1)
	'''

####################
# Edit

def edit (editor,filename):

	if not os.path.exists (filename):
		os.chdir ('u:/tools/bin')

	if not os.path.exists (filename) and filename!="":
		print 'Could not find file: ' + filename
		help ()
		sys.exit(0);

	win32api.WinExec (editor + filename)


####################
# Do Command

word="C:\\Program Files\\Microsoft Office\\Office\\winword.exe "
cw="C:\\Program Files\\CodeWright\\cw32.exe "
notepad="notepad.exe "
vs = '"c:\\Program Files\\Microsoft Visual Studio .NET 2003\\Common7\\IDE\\devenv.com" '
r="U:\\Tools\\ruby\\scite\\scite.exe "

if len(sys.argv)<2:
	win32api.WinExec (notepad)

else:
	editor = sys.argv[1]
	filename = ''
	if len(sys.argv)>2:
		filename=sys.argv[2]
		
	if editor == "-user":
		edit(notepad, "c:/users/user.htm")

	elif editor == "-unload":
		edit(vs, "c:/users/cvs/Unloader/unload/build.sln")

	elif editor == "-caddis":
		edit(vs, "c:/users/cvs/caddis/src/caddis.sln")

	elif editor == "-ephoto":
		edit(vs, "C:/Users/Web/cdi1/ephotoservice/ephotoservice.sln")

  	elif editor == '-n':
		edit(notepad, filename)
		
  	elif editor == '-cw':
		edit(cw, filename)

	elif editor == '-w':
		edit(word, filename)
		
	elif editor == '-vs':
		edit(vs, filename)

	elif editor == '-r':
		edit(r, filename)
		
	else:
		edit (notepad, editor)
	

