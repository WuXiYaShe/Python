#--coding:utf-8--
#

cities = {'CA':'San Francisco','MI':'Detroit',"FL":'jacksonville'}
cities['Ny']="new york"
cities['OR']='PortLand'

print cities

def find_city(themap,state):
	if state in themap:
		return themap[state]
	else:
		return "Not Found."

cities['_find'] = find_city

while True:
	print "state? (ENTER to quit)",
	state = raw_input("> ")
	if not state:break

	#this line  is the most important ever! study!
	city_found = cities['_find'](cities,state)
	print city_found