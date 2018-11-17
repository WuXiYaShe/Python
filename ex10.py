#--coding:utf-8--
#

tabby_cat = "\t I'm tabbed in."
persian_cat = "I'm split\non a line"
backslash_cat = "I'm \\a\\ cat."

fat_cat="""
I'll do a list:
\t* Cat foot
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

new_cat='''
do exercise for this:
\t show the tabby:%s
\t show the persian:%s
\t show the backslash:%s
''' %(tabby_cat,persian_cat,backslash_cat)

print new_cat

print "I am 6'2\" tall." # 将字符串中的双引号转义
print 'I am 6\'2" tall.' # 将字符串种的单引号转义