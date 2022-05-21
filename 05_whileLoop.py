from trace import Trace

# While exucution
i=0
# while(i<10):     
#      print(f"your are the grate no. {i}")
#      i+=1 
# while() break and continue     
#a=int(input("please Enter a Number :"))
while(True):    
    if (i+1<5):
        i=i+1
        continue                
    print(f"This is your Number :",i+1,end=" ")
    if(i==45):
        break
    i=i+1
#Exampal
while(True):
    inp=int(input("Enter a Number"))
    if inp>100:
        print("Congrats your have enterted a number greater than 100 \n")
        break
    else:
         print("Try again! \n")    