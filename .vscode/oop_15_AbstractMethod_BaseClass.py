# is program me hum ye samjhate hai ki agar hum ko koi function ko uske child ko define karna hi hoga to hum iska use karte hai.
from abc import ABC, abstractmethod

class shap(ABC):
    @abstractmethod    
    def printData(self):
        return 0 
    
class rectengal(shap):    
    type="rectengal"
    side=4
    def __init__(self):
        self.width=7
        self.height=6          
        
    def printData(self):
        return self.width*self.height  
       
rect=rectengal()
print(rect.printData())
#sh=shap() Direct hum shap ko call nahi kar sakte hai


    
            
