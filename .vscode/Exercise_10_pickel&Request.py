"""pickle and use requests module to download the iris dataset"""

from matplotlib.pyplot import text
import requests
import pickle

data=requests.get("https://archive.ics.uci.edu/ml/machine-learning-databases/iris/iris.data").text

# print(irisList.text)
# l1=data.split("\n")
# #print(l1)
# l2=[item.split(",")for item in l1 if len(item)!=0]
# #print(l2)
# with open("myIris.pkl",'wb') as f:
#     pickle.dump(l2,f)


file="myIris.pkl"
with open("myIris.pkl",'rb') as f:
    print(pickle.load(f))
