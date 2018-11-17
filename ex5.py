#--coding:utf-8--
#

my_name = 'Gan lubin'
my_age = 20  #活力十足的年轻人
my_height = 170 #cm
my_weight = 147 #kg
my_eyes = 'black'
my_teeth = 'white'
my_hair = 'black'

print "Let's talk about %s." %my_name
print "He's %d inches tall." %my_height
print "He's %d pounds heavy." %my_weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair."%(my_eyes,my_hair)
print "His teeth are usually %s depending on the coffee."%my_teeth
#this line is tricky,try to get it exactiy right
print "If I add %d,%d, and %d I get %d" %(my_age,my_height,my_weight,my_age+my_height+my_weight)
print "\n"
print "show a numbers %r and a string %r."%(my_age,my_eyes)
print "\n"

# 例：数字格式化
nYear = 2018
nMonth = 8
nDay = 18
# 格式化日期 %02d数字转成两位整型缺位填0	
print '%04d-%02d-%02d ' %(nYear,nMonth,nDay)	
# 输出结果 2018-08-18