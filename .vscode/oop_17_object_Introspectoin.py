import email
#lac 70
# find out of type of class and object that is called object introspection

class Employee:
    def __init__(self,fname,lname) -> None:
        self.fname=fname
        self.lname=lname
        #self.email=f"{self.fname}.{self.lname} @ kksinghgmail.com"        
    def explain(self):
        return f"This Employee is {self.fname}.{self.lname}"
    @property
    def email(self):
        if self.fname==None or self.lname==None:
            return "Email is not set please set using setter"
        return f"This Employee is {self.fname}.{self.lname} @ kksinghgmail.com"
    @email.setter
    def email(self,string):
        print("setting")
        names=string.split("@")[0]
        #name=string.split("@")[1]
        self.fname=names.split(".")[0]
        self.lname=names.split(".")[1]
        
    @email.deleter
    def email(self):
        self.fname=None
        self.lname=None  
        
        
skilf=Employee("skill","F")      
#print(skilf.email)
#find tha type of skilf object  this is called Introspection
print(type(skilf))
o="this is a string" 
print(id(o))
# what work done one this object select and use
print(dir(skilf))
# what work done is that string select and use
#print(dir(o)) 
import inspect
print(inspect.getmembers(skilf))
# pleas serch a google and inspect modul in google
