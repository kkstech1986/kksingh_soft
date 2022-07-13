import pickle

#picklin a python object
# cars=["Audi","BMW","Mruti","Suzuki","Maruti Tusuzuki"]
# file= "mycar.pkl"
# fileobj=open(file,'wb')
# pickle.dump(cars,fileobj)
# fileobj.close()

file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
print(mycar)
print(type(mycar))

