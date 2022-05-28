
# Operator to function maping  this to called operator overloading  in class
class Employee:
    LeaveDetails=20     
    def __init__(self,name,salary,department) -> None:
        self.Name=name
        self.salary=salary
        self.Department=department    
     
     ################################print data as formate in many time##############################
    
        
    @classmethod 
    def chengeleave(cls,newLeave):
        cls.LeaveDetails=newLeave 
    def printdata(self):
        return print(f"Yoyr Name : {self.Name}, salary are : {self.salary} and department of {self.Department} ,leave :{self.LeaveDetails}")     
        
      
    def __add__(self,other): #Operator overloading
        return self.salary+other.salary    
  
    def __truediv__(self,other):
        return self.salary/other.salary
    def __repr__(self):
         return f" Employee :('{self.Name}',{self.salary},'{self.Department}')"
     
    def __str__(self):
        return f"Yoyr Name : {self.Name}, salary are : {self.salary} and department of {self.Department} ,leave :{self.LeaveDetails}"
        
    
emp=Employee("kksingh",20000,"service")
# emp1=Employee("Pawan",15000,"programmer")
# print(emp+emp1)
# print(emp/emp1)
#emp.printdata()
print(str(emp))


        