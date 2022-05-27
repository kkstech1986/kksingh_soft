#lac-62
class Employee:
    LeaveDetails=20     
    def __init__(self,name,salary,department) -> None:
        self.Name=name
        self.salary=salary
        self.Department=department    
     
     ################################print data as formate in many time##############################
    def printdata(self):
        print(f"Yoyr Name : {self.Name}, salary are : {self.salary} and department of {self.Department} ,leave :{self.LeaveDetails}")
    ################################ chenge class varialbe by using of class instance and class also  this is chenge value of class variable ############################    
    @classmethod 
    def chengeleave(cls,newLeave):
        cls.LeaveDetails=newLeave  
     ################################Split stiring and return as a list and than pass a class instance value/object and same to send class init constructor##############################   
    @classmethod
    def fromeString(cls,string):
        empobj=string.split("-")
        print(empobj)
        #return cls(empobj[0],empobj[1],empobj[2]) # Traditional type value send to class by list index one by one
        return cls(*string.split("-")) # this is one liner fucton use method of *args *queargs if not understand please see the video of * arge of code with harry in python

class player():
     def playing():
         print("playing a very nice cricket in indian creat leage")
         
class programmer(player,Employee):
    def Cool_programmer():
        print("playing Cricket and and very good programmer in python")
        
        
p=programmer
p.playing()
        
        
                
                                