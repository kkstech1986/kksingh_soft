#creat a dictionary and take input from the user an return the menin of the word from the dictonary


AtoZ={"A":"Appal","B":"Ball","C":"Cat","D":"Doge","E":"Elephant","F":"Fish","G":"Gote","H":"Hen","I":"Ink","J":"Jug","K":"Kite","L":"Leep","M":"Monkey","N":"Nest","O":"Orange","P":"peacock","Q":"Queen","R":"Rabit","S":"Ship","T":"Tiger","U":"Umbrella","V":"Van","W":"Watch","X":"Xylopbon","Y":"Yak","Z":"Zebra",}
print ("pleas Enter the 1 for play game 2 for qute program")

inp=input("Please Enter your choice:")
if inp=="1"and "2":
    if int(inp)==2:
        print("Thanks for next time")
        quit()        
    elif int(inp)==1:
        
     for i in range(27):     
        a=input("Please Enter A To Z Word and find Meaning :")
        
        if a==""and 1!=len(a):
            print("please enter Only A to Z seprate word")
            continue        
        else:
            
            b=a.upper()
            c=AtoZ.get(b)
            print(f"{b} for {c}")
            i=+i 
     print("Thanks for play game")  
elif inp=="":
    print("You are not Enter any choise")
    
else:
    print("Please Enter a valide choise")
        
    
    
        
    

    
    
    