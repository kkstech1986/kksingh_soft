


# list1=[["kksingh",1],['pawan',12],['daw',23],['saroj',4],['nilam',5],['manti',250]]
# print(list1)
# dict1=dict(list1)
# print(dict1)
# for item ,lollypop in dict1.items(): # thai is loop concept 
#     print(item,"and lolly is ",lollypop)
    

# first your make a list and given value that value are any thing no matter but you make a program to fetch data from list number only and biger then 6 
from pandas import value_counts


list2 = [12 ,234,56, 2, 3,"Tata",40]
list3=[23,"ram","syam",12,23,56,789,7,1,2,3,"krishna"]
print(list3)
numbers = []
for item in list3:

   if str(item).isnumeric() and item>6 :
         list5=[]
         list5.append(item)
         print(list5)

   
        
    