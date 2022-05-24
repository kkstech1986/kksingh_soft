from json.tool import main


list1=["64","34","67","3","4"]

# for i in range(len(list1)):
#     for item in list1:        
#         number1=int(item)
#         print(number1)
        
def liprint():
    for item in list1:        
      number1=int(item)
      print(number1)        
    #return number1
    
def har(string):
  return f"Ye print kksingh ko de de thakur {string}"  
 
def add(a,b):
    return a+b+5
  
print ("and the name is",__name__)

if __name__=='__main__' :
      print(har("Suresh"))  
      b=add(4,5)  
      print(b)