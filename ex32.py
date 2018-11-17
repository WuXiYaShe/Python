#--coding:utf-8--
#list
the_count = [1,2,3,4,5]  
fruits = ['apples','oranges','pears','apricots']
change = [1,'pennies',2,'dimes',3,'quarters']

# 通过列表进行第一次循环列表
for number in the_count:
	print "This is count %d" %number

# same as above
for fruit in fruits:
	print "A fruit of type: %s" %fruit
	
#also we can go through mixed lists too
#notice we have to use %r since we don't know what's in it
for i in change:
	print "I got %r" %i


#we can also build lists,first start with an empty one
elements = []

#then use the range function to do 0 to 5 counts
for i in range(0,6):
	print "Adding %d to the list." %i
	#append is a function that lists understand
	elements.append(i)

#now we can print them out too
for i in elements:
	print "Elements was: %d" %i

#range(start， end， scan): 
#start：计数从start开始，默认为0，range(2)=range(0,2) 
#end： 计数到end结束 list(range(2))为[0,1] 注意包左不包右！ 
#scan: 计数的步长，默认为1，可以指定 比如range(0,4,2)
