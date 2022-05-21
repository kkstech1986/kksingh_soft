# pattern printing 
# input =integer n
# boolen= True or False

n=int(input("Enter a integer valu for print Star pattern :"))
      
sbool=bool(input("print for desending order press 1 : \n"))
# for i in range(n):
     
#      for j in range(n+1)
#          print(j*"*")
     
# for i in range(n+1):
#     print(i*"*") 

if sbool==True:
     
    i=1    
    for i in range(n+1):
        print((n-(n-i))*" * ")  

if sbool==False:
        
    for i in range(n+1):
        print((n-i)*" * ")        