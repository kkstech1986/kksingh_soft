class A:
    classvar1="I am a class variable in class A"
    def __init__(self) -> None:
        self.var1="I am inside class A 's constructor\n"
        self.classvar1="Instance var in class A"
        self.spaceal="special\n"
        
class B(A):
    
    classvar1="I am a class variable in class B"
    def __init__(self) -> None:
        
        self.var1="I am inside class B 's constructor\n" 
        #self.classvar1="Instance var in class B"
        super().__init__() # method over-ride in this classA
        print(super().classvar1)
           
        
        
a=A()
b=B()
print(b.classvar1) 
''' agar hum isko print karte hai to sabse pahle ye class B me instance variable Khojega nahi milega to wah calss A me instance variable Khojega 
agar waha hai to print karega Agar class A me instance verialble nahi melaega to wah pbir se class B me ayega and waha instacnce verialbe
khojega waha hai to print karega agar nahi hai to pir wah class A me gayega aur agar waha hai to print kar dega.'''

print(b.spaceal,b.var1,b.classvar1)  

'''This call after method over riding'''



       