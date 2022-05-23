# recurtion function work as n*recurtion(n-1)
# iterative function work as n=n*n(n-1)
#5x4x3x2x1=

from math import factorial
#inbult factorial 
b=factorial(7)
print(b)
# with buld fuction by programmer
def factorial_Iterative(n):
    fac=1
    for i in range(n):
        fac=fac*(i+1)
    #print("Your recurtion value of : ",fac)
    return fac  

number=int(input("Please Enter a Number"))
print("Fcotirial Number is :  " , factorial_Iterative(number))
# a=factorial_Iterative(7)   
# print(a)
# Factorial for recurtion
def Factorial_recurtion(n):
    fac=1
    i=1
    if n==1:
        return 1
    else:
        for i in range(n):
            fac=n*Factorial_recurtion(n-1)
    #print("Your recurtion value of : ",fac)
    return fac    

# Right a febonacho series for ei. 0,1,1,2,3,5,8,13

def febonachoSeries(n):
    
    if n==1:
        return 0
    elif n==2:
        return 1
    else:
        return febonachoSeries(n-1)+febonachoSeries(n-2)    
    
c=febonachoSeries(7)
print(c) 
b=Factorial_recurtion (7)   
# print(b) 