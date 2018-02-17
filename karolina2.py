#!/usr/bin/python
import os
f=os.popen("cat /proc/cpuinfo|grep processor")
x=f.read()
y=x.split('\n') #zrobilismy liste
print y
print len(y)
