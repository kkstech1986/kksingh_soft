# pattern printing 
# input =integer n
# boolen= True or False


try:
    n=int(input("Enter a integer valu for print Star pattern :"))         
    sbool=input("print for desending order press 1 & Assending order press 2 : ")
    if sbool=="1":     
        i=1    
        for i in range(n+1):  print((n-(n-i))*" * ") 
        print("Thanks for printing star pattern ")    
    elif sbool=="2":
        for i in range(n+1):  print((n-i)*" * ")
        print("thanks for print Star patter ")  
    else:
            
        for i in range(n+1):  print((n-(n-i))*" * ")
        for i in range(n+1):  print((n-i)*" * ")        
        print("you are not select order both are prited")              
except Exception as e: print("please Enter Integer value ei 1,2,3,4,5,6,7,8")   
# with two nos for loop use  
# if sbool=="1":
#     for i in range((n+1)):
#         j=1
#         for j in range(j):
#             #print(j)
#             print("*"* i)
        
# elif sbool=="2":
#     for i in range((n+1)):
#         j=1
#         for j in range(j):
#             #print(j)
#             print((n-i)*"*")
    
            


         
    
                       


        
        