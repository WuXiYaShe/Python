#--coding:utf-8--
#

ten_thing = "Apples Oranges Crows Telephone Light Sugar"
print "Wait these's not  10 thing in that list,let's fix that."
stuff = ten_thing.split(' ')
more_stuff = ["Day","Night","Song","firsbee","Corn","Banana","Girl","Boy"]

while len(stuff) != 10:
	next_one = more_stuff.pop()
	print "Adding: ",next_one
	stuff.append(next_one)
	print "There's %d intms now.",len(stuff)

print "There were we go: ",stuff
print "let's do some things with stuff."

print stuff[1]
print stuff[-1]  #whoa! fancy!
print stuff.pop()
print ' '.join(stuff)  #what? coll!
print '#'.join(stuff[3,5]) 