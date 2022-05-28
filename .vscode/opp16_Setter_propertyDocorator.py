import email
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
    
Hindustani_sapotar=Employee("Hindustani","Supporter")
print(Hindustani_sapotar.email)
# chenge only chenge fname by using by setter
Hindustani_sapotar.fname="us"
print(Hindustani_sapotar.email)
# chenge only chenge fname by using by setter
Hindustani_sapotar.email="this.that@kksingh.com"
print(Hindustani_sapotar.email)
# set deleter 
del Hindustani_sapotar.email
print(Hindustani_sapotar.email)




        
    