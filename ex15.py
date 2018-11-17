#--coding:utf-8--
#

#sys 是一个代码库，这句话的意思是从库里取出 argv 这个功能来，供我使用
from sys import argv
#获取参数 给script赋值ex15.py  filename赋值ex15_sample.txt
script,filename = argv

#	# 打开 ex15_sample.txt
#	txt = open(filename)
#	#打印 Here's your file ex15_sample.txt
#	print "Here's your file %r:"%filename
#	#打印 ex15_sample.txt 文本内容
#	print txt.read()  

#打印 Type the filename again:
print "type the filename again:"
#输入 为file_again赋值
file_again = raw_input('> ')
#打开 file_again文本
txt_again = open(file_again)
#打印 file_again文本
print txt_again.read()