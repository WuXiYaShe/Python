#--coding:utf-8--
#

from sys import argv
from os.path import exists

scripts,form_file,to_file = argv

print "This is the scripts : %r" %scripts
print "Coping from %s to %s" %(form_file,to_file)

#打开from_file文件   读取form_file文件内容   值传递给indata
input = open(form_file)
indata = input.read()

#len() 方法返回对象（字符、列表、元组等）长度或项目个数。
print "The input file is %d bytes long" %len(indata)

#exist 将文件名字符串作为参数，如果文件存在的话，它将返回 True，否则将返回 False
print "Does the output file exists? %r" %exists(to_file)
print "Ready,hit RETURN to continue,CTRL-C to abort"
raw_input('> ')

#打开to_file文件,提供写操作    
output = open (to_file,'w')
#将indata值写入to_file
output.write(indata)

print "Alright ,all done."
#处理完文件后将其关闭
output.close()
input.close()