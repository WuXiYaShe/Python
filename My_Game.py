#coding=utf-8
#这是我自己写的一个游戏

def Bedroom():
	print "\n\tWhen you get up, you find the bedroom dark, and you are eager to know what has happened."
	print "\tYou have three choices:\n\t1.Bedroom_door \n\t2.Bedroom_window \n\t3.Bedroom_drawer"
	next = raw_input(">>>")
	if next == "1":
		print "**************************"
		print "The bedroom door is closed."
		Nokey_bedroom()
	elif next == "2":
		print "***********************************"
		print "There's nothing outside the window."
		Nokey_bedroom()
	elif next == "3":
		print "*********************************************"
		print "The key to the bedroom door is in the drawer."
		Key_bedroom()
	else :
		Death()

def Nokey_bedroom():
	print "\tYou have three choices:\n\t1.Bedroom_door \n\t2.Bedroom_window \n\t3.Bedroom_drawer"
	next = raw_input(">>>")
	if next == "1":
		Death()
	elif next == "2":
		print "***********************************"
		print "There's nothing outside the window."
		Death()
	elif next == "3":
		print "*********************************************"
		print "The key to the bedroom door is in the drawer."
		Key_bedroom()
	else :
		Death()

def Key_bedroom():
	print "\tYou have three choices:\n\t1.Bedroom_door \n\t2.Bedroom_window \n\t3.Bedroom_drawer"
	next = raw_input(">>>")
	if next == "1":
		print "*************************************"
		print "The bedroom door is open by the key."
		Living_room()
	elif next == "2":
		Death()
	elif next == "3":
		Death()
	else :
		print "*********************************"
		print "Fools, you made a wrong decision."
		Death()

def Death():
	print "You've been attacked behind the back. The game is over."
	print "********************************************************"
	exit(0)

def Living_room():
	print "\tThere are lighted candles on the dining table in the middle of the living room."
	print "\tWhen you get close to it, you find:"
	print "\tEscape as soon as possible!!!"
	print "\tYou have three choices:\n\t1.Front_door \n\t2.Kitchen_door \n\t3.TV_cabinet"
	next = raw_input(">>>")
	if next == "1":
		Death()
	elif next == "2":
		Kitchen_room()
	elif next == "3":
		print "****************************"
		print "You found a good flashlight."
		Light_Living_room()
	else :
		Death()
	
def Light_Living_room():
	print "\tYou have three choices:\n\t1.Front_door \n\t2.Kitchen_door \n\t3.TV_cabinet"
	next = raw_input(">>>")
	if next == "1":
		print "*******************************"
		print "You found the trap at the door."
		Circle_Living_room()
	elif next == "2":
		print "*************************"
		print "You found a set of tools."
		fianl_Living_room()
	elif next == "3":
		Death()
	else:
		Death()

def Dark_Living_room():
	print "\tYou have three choices:\n\t1.Front_door \n\t2.Kitchen_door \n\t3.TV_cabinet"
	next = raw_input(">>>")
	if next == "1":
		Death()
	elif next == "2":
		Death()
	elif next == "3":
		print "****************************"
		print "You found a good flashlight."
		Light_Living_room()
	else:
		Death()


def Circle_Living_room():
	print "You have three choices:\n\t1.Front_door \n\t2.Kitchen_door \n\t3.TV_cabinet"
	next = raw_input(">>>")
	if next == "1":
		print "You are trapped by the trap. The game is over."
		print "***********************************************"
		exit(0)	
	elif next == "2":
		print "*************************"
		print "You found a set of tools."
		fianl_Living_room()
	elif next == "3":
		Death()
	else :
		Death()


def Kitchen_room():
	print "*************************"
	print "You can't see anything."
	Dark_Living_room()


def fianl_Living_room():
	print "You have three choices:\n\t1.Front_door \n\t2.Kitchen_door \n\t3.TV_cabinet"
	next = raw_input(">>>")
	if next == "1":
		print "You use tools to remove traps and save yourself.Good Luck!"
		print "**********************************************************"
		exit(0)	
	elif next == "2":
		Death()
	elif next == "3":
		Death()
	else :
		Death()


Bedroom()


