#--coding:utf-8--
#

from sys import argv #(argument variable)

scripts,user_name = argv 
prompt = '> '

print "Hi %s,I'm the %s scripts." %(user_name,scripts)
print "I'd like to ask you a few questions"
print "Do you like me %s ?"%user_name
likes = raw_input(prompt)

print "Where do you live %s ?"%user_name
lives = raw_input(prompt)

print "What kind of computer do you have ?"
computer = raw_input(prompt)

print """
Alright,so you said %r about liking me.
You live in %r .Not sure where that is.
and you have a %r computer . nice.
""" %(likes,lives,computer)
