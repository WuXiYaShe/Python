#--coding:utf-8--
#

#你需要把 sys 模组 import 进来
from sys import argv
#把 argv中的东西解包，将所有的参数依次赋予左边的变量名
script,first,second,third = argv

print "The script is called:",script
# print "Your first variable is:",first
# print "Your second variable is:",second
# print "Your third variable is:",third

first = raw_input("Your first variable is:")
second = raw_input('Your second variable is:')
third = raw_input('Your third variable is:')

print "1.%r\n2.%r\n3.%r"%(first,second,third)
