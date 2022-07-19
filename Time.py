import re
from unittest import result


class time:

    def __init__(self,h,m,s):
        self.hour=h
        self.minute=m
        self.second=s

    def sum(self,x):
        result=time(None,None,None)
        result.second=self.second+x.second
        result.minute=self.minute+x.minute
        result.hour=self.hour+x.hour 
        if result.second>=60:
            result.second-=60
            result.minute += 1
        if result.minute>=60:
            result.minute-=60
            result.hour += 1
        return result    
           
    def sub(self,x):
        result=time(None,None,None)
        if self.second<x.second:
            self.second+=60
            self.minute-=1
        result.second=self.second-x.second
        if self.minute<x.minute:
            self.minute+=60
            self.hour-=1
        result.minute=self.minute-x.minute
        result.hour=self.hour-x.hour 
        return result 

    def s2time(self):
        result=time(0,0,0)
        result.hour=self.second//3600
        b1=self.second%3600
        result.minute=b1//60
        result.second=b1%60
        return result

    def time2s(self):
        result=time(0,0,0)
        result.second=self.second+(self.minute)*60+(self.hour)*3600
        return result

    def show(self):
        print(self.hour, ':',self.minute,':',self.second)

A=time(3,6,28)
B=time(1,55,32)  

A.show()
B.show()


c=A.sum(B)
c.show()

d=A.sub(B)
d.show()

e=A.time2s()
e.show()

g=e.s2time()
g.show()