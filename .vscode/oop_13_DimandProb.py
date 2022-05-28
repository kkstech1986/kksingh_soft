

class A:
    def met():
     print("This is a Method form class A")
class B(A):
    def met():
     print("This is a Method form class B")
    
class C(A):
    pass
    
    # def met():
    #  print("This is a Method form class c")
    
class D (C,B):
    pass
    
    # def met():
    #  print("This is a Method form class D")
         
         
         
d=D

print(d.met())        
    

    