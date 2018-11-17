#--coding:utf-8--
#

#sys 是一个代码库，这句话的意思是从库里取出 argv 这个功能来，供我使用
from sys import argv
#获取参数 给script赋值ex16.py  给filename赋值...
scripts,filename = argv

print "this is scripts:%r"%scripts

#打开文件...
filename_txt = open(filename)
#读取文件内容
print filename_txt.read()
