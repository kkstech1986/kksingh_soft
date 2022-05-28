# Access Specifiare in python verialble are public,protected & private 
class Student():        
    _subject=["Hindi","English","Math","Science"]    
    def __init__(self,name,age,gender,roll) -> None:
        self.Name=name
        self.Age=age
        self.Gender=gender
        self.Roll=roll   
    def printdata(self):           
           print(f"Your Name: {self.Name},Age is :{self.Age},Gender is :{self.Gender},Roll no is {self.Roll},your hobby is {self.Hobby},runnig {self.Runnig}")                        

class Teacher(Student):    
    __Sports=["Cricket","Footbal","Hoky",] 
    def __init__(self, name, age, gender, roll,hobby) -> None:
        super().__init__(name, age, gender, roll)        
        self.Hobby=hobby              
class Exercise(Teacher):
    __Exercise=("Anulom_Bilom","SuryaNamaskar","Chakrasan","Runnig")  
    def __init__(self, name, age, gender, roll, hobby,runnig) -> None:
        super().__init__(name, age, gender, roll, hobby)    
        self.Runnig=runnig    
    def printdata(self):
        print(f"Your Name: {self.Name},Age is :{self.Age},Gender is :{self.Gender},Roll no is {self.Roll},your hobby is {self.Hobby},runnig {self.Runnig}")
        #return f"Your Name: {self.Name},Age is :{self.Age},Gender is :{self.Gender},Roll no is {self.Roll},your hobby is {self.Hobby},runnig {self.Runnig}"
          
ex=Exercise
kks=ex("Krishna Kumar",34,"male",123,"cricket","100 miter")   
pks=Exercise("pawan Kumar",30,"male",120,"cricket","10 miter")
kks.printdata() 
pks.printdata()  
print(pks._subject)
print(pks._Teacher__Sports)
print(pks._Exercise__Exercise)


  

        
        
    
        