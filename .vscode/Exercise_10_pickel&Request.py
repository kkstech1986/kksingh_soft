"""pickle and use requests module to download the iris dataset"""

import json
from typing import Type
import requests
import pickle
irisList=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data")
#print(irisList.text)

# file="irisDatalist.txt"
# fileobj=open(file,'w')
# fileobj.writelines(irisList.text)
# fileobj.close()

file="irisDatalist.txt"
fileobj=open(file,"r")
kks=fileobj.readlines()
fileobj.close()
print(kks)
print(type(kks))

file1="irisData.pkl"
filobj1=open(file1,"wb")
pickle.dump(kks,filobj1)
fileobj.close()

file1="irisData.pkl"
filobj1=open(file1,"rb")
mydata=pickle.load(filobj1)
fileobj.close()
print(mydata)
print(type(mydata))
