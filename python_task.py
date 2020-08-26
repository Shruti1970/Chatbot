import os
import pyttsx3 as spk
import webbrowser
import datetime


hour = int(datetime.datetime.now().hour)

if hour>=0 and hour<12:
   spk.speak("Bonjour utilisateur!")
elif hour>=12 and hour<18:
   spk.speak("bonne après-midi utilisateur!")
else :
   spk.speak("Bonsoir utilisateur!")
print("******************************************************************************************")
print("                     BIENVENUE DANS MON MONDE MAGIQUE                                      ")
print("*******************************************************************************************")

spk.speak(" Welcome to the magic world , Please tell me how may I help you")
    

def speaker(param):
	spk.speak("I Got it sir..."+param+"...launching for you!")


while True:
	print("I can do the magic on the following attributes of your system")
	print("Wanna do calculations.....say calculator")

	print("Say .. you want to watch videos...checkout on youtube ")

	print("Want to write some text.. say notepad ")

	print("Love to paint.....say paint ")

	print("Like to surf internet....say google ")


	a = input(" Make a wish : ")
	if ("notepad" in a):
		y = "notepad"
		speaker("notepad")
		os.system(y)
		print(y+ "..LAUNCHED..")
	elif ("calculator" in a):
		y = "calc"
		speaker("calculator")
		os.system(y)
		print(y+ "..LAUNCHED..")
	elif ("youtube" in a):
		spk.speak("Opening youtube for you sir")
		webbrowser.open("youtube.com")
	elif ("paint" in a):
		y = "mspaint"
		speaker("Paint")
		os.system(y)
		print(y+"..LAUNCHED..")
	elif ("google" in a):
		spk.speak("Opening google for you sir")
		webbrowser.open("google.com")

	elif ("exit" in a):
		y = "exit"
		spk.speak("merci s'il vous plait revenez")
		print("Thank you please come again")
		break
	else:
		spk.speak("Sorry sir , Something is wrong! Try again")
		print("Oops!!!Not allowed to do this, make another wish")