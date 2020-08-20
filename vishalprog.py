import pyttsx3 as p
import os
while True:
	print("chat with me with your requirements : "  , end='')
	p = input()

	# print(p)
	# os.system(p)

	if ("run" in p)  and ("chrome" in p):
	  os.system("start chrome")

	elif ("run" in p)  and ("firefox" in p):
	  os.system("start Firefox")

	elif (("run" in p) or  ("execute" in p )) and  (("notepad" in p) or ("editor" in p) ) :
	  os.system("notepad")

	elif ("run" in p)  and ("player" in p) and ("media" in p):
	  os.system("start wmplayer")
	  
	elif ("run" in p)  and ("camera" in p):
	  os.system("start microsoft.windows.camera:")
	  
	elif ("run" in p)  and ("calculator" in p):
	  os.system("start calculator:")

	

	

	elif  ("exit" in p)  or ("quit" in p):
	  break

	else:
	  print("dont support")


