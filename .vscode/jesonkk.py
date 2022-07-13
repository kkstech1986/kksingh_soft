import json
#json=Java script object notation
data='{"var1":"Krishna","var2":56}'
print(data)
#print(data['var1']) #This is wrong this is not prosible for "String idices must be integers"
parsed=json.loads(data)
print(data)
print(parsed['var1']) # jabki ye json me parsed karte hai to ye print alag alag ho jata hai jabki ye dicsnary me nahi hai.
print(type(parsed))
# Task i- json, load ?

data2={
    "chenal Name" : "CodeWithHarry",
    "cars":["Bolloro",'auds a8','fararay'],
    "frize":('roti',540),
    "isbad": False
}

jscomp=json.dumps(data2)
print(jscomp)