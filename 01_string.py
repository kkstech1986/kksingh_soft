
from itertools import count
from operator import countOf
from re import A


str="krishna Kumar singh is very Good Coder for C#,C++,C and Python this for coming future in the world,so this "
str2=["krishna Kumar singh is very Good Coder for C#,C++,C and Python this for coming future in the world,so this ",'is','is','is']
str3=[1,2,3,3,4,4]
#str="this is"
print(type(str))
str1=str.capitalize()
# print(str1)
# a=str.endswith("is")
# print(a)
b=countOf(str2,"is")
print(b)
n=str2.count('is')
print(n)

print(str)
print(str1)
print(str3)
