d1={}
print(type(d1))
d2={"kksingh":"Burger","sohan":"Fish","subham":{"b":"Maggi","L":"Roti","d":"Chicken"},"pawan":"Rice"}
d2["Ankit"]="junks food"
d2["Suresh"]="egg"
print(d2)
print(d2["subham"]["b"])
del  d2["Suresh"]
print(d2)
# use copy function to saprate copy make if you use d3=d2 this is not seprate copy this is a pointer so that you are delete the item in d3 same item are delete in d2 also but this is not happend in if you use d.copy function
d3=d2.copy()
#d3=d2
del d3['kksingh']
d2.update({"lina":"rice"})
print()
print(d2)
print(d3)
#print(d2.keys())
print(d2.items())

