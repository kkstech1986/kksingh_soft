from logging import exception


# print("Enter num 1")
# num1= int(input())
# print("Enter num 2")
# num2=int(input())

# print("The sum of these two number is :"
#       ,num1+num2)


print("Enter num 1")
num1= input()
print("Enter num 2")
num2=input()
try:
    print("The sum of these two number is :"
        ,int(num1)+int(num2))
    
except Exception as e:
    print(e)
    
print("This line is very mostimportant")        