#--coding:utf-8--
#

i = 0
numbers = []
while i<6:
	print "At the top i is %d"%i
	numbers.append(i)
	i = i + 1
	print "Numbers now:",numbers
	print "At the bottom i is %d" %i
print "The numbers:"
for num in numbers:
	print num
print "\n"

def while_function(i,increment):
	j = 0
	numbers=[]
	while j < i:
		numbers.append(j)
		j += increment
	return numbers

numbers = while_function(6,2)	
print numbers
print "\n"

def for_function(i,increment):
	numbers = []
	for j in range(0,6,increment):
		numbers.append(j)
	return numbers

numbers = for_function (6,1)
print numbers
print "\n"