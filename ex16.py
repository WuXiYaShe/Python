#--coding:utf-8--
#

#sys 是一个代码库，这句话的意思是从库里取出 argv 这个功能来，供我使用
from sys import argv
#获取参数 给script赋值ex16.py  给filename赋值...
script,filename = argv

print "We'll new build a file with name: %r." %filename
print "If you don't want that, hit CTRL_C(^C)."
print "if you do want that ,hit RETURN."

#print "?"
#raw_input()
raw_input("?")


print "Opening the file..."
# 打开 ...文件
target = open(filename,'w')
print "Truncating the file, Goodbuy!"
# 清除该文件内容
target.truncate()

print "Now I'm going to ask you for three lines."
#输入三行内容
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."
#三行内容写入文件
target.write(line1)
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally, we close it."
#关闭文件
target.close()