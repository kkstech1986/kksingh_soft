from itertools import count
import random


# Snake water Gun
#var1=("snake","water","gun")
# print(sysVar1)
def takvar(s):
    if s==1:
        return "snake"
    elif s==2:
        return "water"
    elif s==3:
       return "gun"    
print("You are select 1=snake,2=water,3=gun")
Point=0
SysPoint=0
Taiscor=0    
for i in range(5):
    sysval=random.randint(1,3)
    c=takvar(sysval)
    #c="water"
    #print(c)   
    var2=int(input("Enter your choise : "))
    a=takvar(var2)
    #print(a)     
    if c=="snake" :        
        if a=="gun":
            print("Your winer")
            Point=Point+1             
        elif a=="water":
            print("you looser")
            SysPoint=SysPoint+1
        else:
            print( " score tai")
            Taiscor=Taiscor+1
    elif c=="gun":        
        if a=="water":
            print("Your winer")  
            Point=Point+1             
        elif a=="snake":
            print("you looser")
            SysPoint=SysPoint+1
        else:
            print( " score tai")
            Taiscor=Taiscor+1
    elif c=="water":
        if a=="snake":
            print("Your winer")
            Point=Point+1               
        elif a=="gun":
            print("you looser")
            SysPoint=SysPoint+1
        else:
            print( "score tai")
            Taiscor=Taiscor+1     
print(f"Your points: {Point}|| Computer points: {SysPoint}||Score tai: {Taiscor}")
print("Thanks for paying a game")          
               
         
     
     
    
    