#--coding:utf-8--
#

from sys import argv
script,input_file = argv

def print_all(f):
	print f.read()

def rewind(f):
	f.seek(0)   
#seek函数作用是： 移动文件的读取指针到指定位置。seek函数需要使用文件对象进行调用，无返回值。

def print_a_line(line_coint, f):
	print line_coint,f.readline()

current_file = open(input_file)

print "First let's print the whole file:\n"
print_all(current_file)

print "Now let's rewind ,kind of like a tape.\n"
#如果不读取指针位置 接下来三行为空
rewind(current_file)

print "Let's print three lines:"
current_line = 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)

current_line += 1
print_a_line(current_line,current_file)