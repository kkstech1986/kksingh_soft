from email.contentmanager import raw_data_manager
from pickle import APPEND


class decor:
    grantleave=12
    def __init__(self,name,roll,subject):
        self.name=name
        self.roll=roll
        self.subject=subject 
        
    def printdata(self):
        print(f"Your name:  {self.name} , Roll Number : {self.roll} , \n  your subject : {self.subject}") 
            
            

          
de=decor
dc=decor
a=de("kksingh",121,["Hindi","English","Math","Economics","Science"])

b=de("Pawan Kumar",122,["Hindi","English","Math","Economics","Science","Geography"])
c=dc("Daw Kumar",122,["Hindi","English","Math","Economics","Science","Geography"])
# a="rama"
# b="shyama"
calactdata={"st1": a,"st2":b}

#print(dc.__dict__)

print(decor.__dict__)

# de.printdata(a)
# de.printdata(b)
# dc.printdata(c)



             
         
    