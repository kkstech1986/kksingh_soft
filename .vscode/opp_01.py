
from re import A
class student: # class is a template just a corbon copy /this is a structure  instance is real object of class 
    
    statudentLeave=10 # class variable
    def printname():
        print("kksingh is good boy")    
        a= "kksingh is boy"   # if this line not write and send to return massege send in time of use fuctin "None" print are show "kksingh is a good boy"
        return  a   # if return massege  not write in function function terurn type is "None"
    
kks=student # Creat instance of  student class 
pawan=student # Creat instance of  student class 
pawan.name="pawan Kumar Singh"  # class instance variable 
pawan.Roll=100 # class instance variable
pawan.subject=["hindi","Math","English","Sanskrit"] # class instance variable
kks.name="Krishna Kumar Singh" # class instance variable
kks.Roll=110 # class instance variable
kks.subject=["hindi","Math","English","Sanskrit"] # class instance variable
kks.statudentLeave # this is class variable use by class instance ei kks 
pawan.__dict__()
print(pawan.name,pawan.Roll,pawan.subject)
print(kks.name,kks.Roll,kks.subject,kks.statudentLeave,kks.printname())

