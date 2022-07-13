from matplotlib.pyplot import get
import requests

#r=requests.get("https://www.zoominfo.com/c/financialmodellingcom-ltd/352917275")
r=requests.get("https://site.financialmodelingprep.com/developer")
#print(r.text)
print(r.status_code)
# url="www.somthing.com"
# data={
#     "p1" "4",
#     "p2" "8"
# }
# r2=requests.post(url=url,data=data)
