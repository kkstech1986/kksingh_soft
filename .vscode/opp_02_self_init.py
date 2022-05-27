class stu: # class is a template just a corbon copy /this is a structure  instance is real object of class 
    
    studentLeave=10 # class variable
    def printname():
        #print("kksingh is good boy")    
        a= "kksingh is boy"   # if this line not write and send to return massege send in time of use fuctin "None" print are show "kksingh is a good boy"
        return  a   # if return massege  not write in function function terurn type is "None"
    
    def printdetails(self):
        return f" Name is {self.name}, Roll no is {self.Roll},Subject is {self.subject},Student leave {self.studentLeave}"
    
    @classmethod # Decorator method use for chenge value of  calss variable
    def chengestudendtLeave(cls, newleave):
        cls.studentLeave=newleave 
        
kks=stu # Creat instance of  student class
pks=stu # Creat instance of  student class 
kks.name="Krishna Kumar Singh" # class instance variable
kks.Roll=110 # class instance variable
kks.subject=["hindi","Math","English","Sanskrit","Economic"] # class instance variable
kks.studentLeave # this is class variable use by class instance ei kks
pks.chengestudendtLeave(34)
print(stu.printdetails(kks))
pks.name="pawan Kumar Singh"  # class instance variable 
pks.Roll=100 # class instance variable
pks.subject=["hindi","Math","English","Sanskrit"] # class instance variableh
stu.chengestudendtLeave(80)


# print(pks.name,pks.Roll,pks.subject)
# print(kks.name,kks.Roll,kks.subject,kks.statudentLeave,kks.printname())

print(pks.printdetails(pks)) # print data through method 