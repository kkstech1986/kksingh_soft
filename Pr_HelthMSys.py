# Health Managment System
# three person ,KKsingh,Pawan Kumar & Daw Kumar
# Make a three file for Food and three file for Exercise 
#
namelist=["kksingh","pawan","Daw"]
def TakeInp():
    p=input("please Enter Your Name : ")
    if p==" ": 
        print("Pleae Enter  valid Name")
    elif p in namelist:
        return p
    else:
        print("pleae Enter valid name try again : ") 
        print("****************************")
              
        
print("please Enter '1' for Food ,'2' for Exercise and '3' for ShowData")
Food_Exercise=input("Enter your choice as above : ")     
n=TakeInp()       
  
def gatdate():
    
    import datetime
    return str(datetime.datetime.now())    
def food():
    list1=[]
    a=input("Rice/Roti : ")
    list1.append(a)
    b=input("Dal/Chiken/kadi: ")
    list1.append(b)
    c=input("papad/salad: ")
    list1.append(c)
    return str(list1)
def Exersice():
    list2=[]
    a=input("Runnig time : ")
    t=a+ "30 Minits"
    list2.append(t)
    b=input("Surya Namaskar/chakrasan time : ")
    t1=b+ "30 Minits"
    list2.append(t1)    
    c=input("Anulom Bilom/Halasan: " )
    t2=c+ "30 Minits"
    list2.append(t2)    
    return str(list2)   
 
def FoodshowData():
    if n=="kksingh":
        fi1="kksinghFood.txt"
        fi2    ='r'    
    elif n=="pawan":
        fi1="pawanFood.txt"
        fi2='r'
    elif n=="Daw":
        fi1="DawFood.txt"
        fi2='r'            
    with open(fi1,fi2) as f:
        s=f.read()        
        f.close() 
    print("Your Date wise Food Report : \n ",s)  
    
def HealthShowData():
    if n=="kksingh":
        fi1="kksinghHealth.txt"
        fi2    ='r'    
    elif n=="pawan":
        fi1="pawanHealth.txt"
        fi2='r'
    elif n=="Daw":
        fi1="DawHealth.txt"
        fi2='r'            
    with open(fi1,fi2) as f:
        s=f.read()        
        f.close() 
    print("Your Date wise Health Report data \n ",s)            

if n in namelist:
    if Food_Exercise=="1":        
        a=food()
        b=gatdate()
        if n=="kksingh":
            fi1="kksinghFood.txt"
            fi2='a'
        elif n=="pawan":
            fi1="pawanFood.txt"
            fi2='a'
        elif n=="Daw":
            fi1="DawFood.txt"
            fi2='a'            
        with open(fi1,fi2) as f:
            f.write(b)
            f.write(a)
            f.write("\n")
            f.close()
    elif Food_Exercise=="2":
        a=Exersice()
        b=gatdate()
        if n=="kksingh":
            fi1="kksinghHealth.txt"
            fi2='a'
        elif n=="pawan":
            fi1="pawanHealth.txt"
            fi2='a'
        elif n=="Daw":
            fi1="DawHealth.txt"
            fi2='a'
        with open(fi1,fi2) as f:                
         f.write(b)
         f.write(a)
         f.write("\n")
         f.close()
    elif Food_Exercise=="3":
        FoodshowData()
        HealthShowData()     
             
        
        
                
            
                    
            


     