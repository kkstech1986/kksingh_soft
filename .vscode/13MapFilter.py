from ast import Lambda
Numbers1=["45","65","5","7","8"]
# # Numbers1[2]=Numbers1[2]+1 # not pasibale not add int to string
##################################################################################################
# # this work done with user for traditional method but this is not a good way.

for i in range(len(Numbers1)):
    Numbers1[i]=int(Numbers1[i])
    
Numbers1[2]=Numbers1[2]+10   
# print(Numbers1)    
#####################################################################################################    
#  # use map function for convert the entiar list value  string to int  
    
Numbers1=list(map(int,Numbers1))
Numbers1[2]=Numbers1[2]+10
#print(Numbers1[2])
#################################################################################
# # this is user function and lemda  same work done nicly 
def sq(a):
    return a*a 
num=[1,2,3,4,5,5,6,7,]
square=list(map(sq,num ))
#print(square)

########################################################################
# work done with lamda function
num3=[1,2,3,4,5,5,6,7,]
square=list(map(lambda x:x*x,num3 ))
#print(square)

#################################################################################################
# Use lanmda in as a function call function
def squr(a):
    return a*a 
def quebe(a):
    return a*a*a
num1=[squr,quebe]
for i in range(5):
    list1=list(map(lambda x:x(i),num1))    
    #print(list1)        
    
####################################################################################################
# # filter function 
print("Filter fuction out put")
num2=[1,2,3,4,5,5,6,7,8,9,10]
def is_greter_5(num):
    return num>5
gr_than_5=list(filter(is_greter_5,num2))
#print(gr_than_5)
########################################################################################################
from functools import reduce
num3=[1,2,3,4,5,5,6,7,8,9,10,78]
number4=reduce(lambda x,y:x+y,num3)
# number2=0
# for i in num3:
#     number2=number2+i
# print(number2) 
print(number4)    
