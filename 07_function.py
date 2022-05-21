
from numpy import average


a=9
b=8
c=sum((a,b)) # built in function
#print(c)

#user Difined function
def function1(a,b):
    print("Hello you are in function1",a+b)
    
#print(function1())
#function1(5,6)
# Doc String for find a difination of fuction and  what is work 
def function2(a,b):
     '''This is a function which will calculate avrage of two number'''
     '''This function only work in two number'''
     average=(a*b)
     return average     

c=function2(5,6)
print(c)
print(function2.__doc__)

