#file IO  Basics
'''
"r" - open file for reading 
"W"- open a file for writing
"x" -crates file if not exists
"a" - Add more content to a file
"t" - text mode
"b"- Binary mode
"+" - read and write mode

'''  
f=open("kksing.txt",'a')
content=f.write ("kumar singh krishna  pwan kumar \n")
print(content)
f.close()
