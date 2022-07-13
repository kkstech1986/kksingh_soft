import re
mystr='''
91000000
918888888
Tata For Commercial Vehicles
Email Id - cac@tatamotors.com Toll Free Number -1800 209 7979,
For Passenger Vehicles
Email Id - customercare@tatamotors.com Toll Free Number -1800 209 8282,Tata Motors International Business
A Block, Shivasagar Estate,
Dr. Annie Besant Road,
Worli, Mumbai - 400018
Contact: 
91(22) 67577200


Domestic Business
Tata Motors Ltd
4th Floor, Ahura Centre
82 Mahakali Caves Road
MIDC, Andheri East
Mumbai - 400093
Contact: 022 - 62407101 aiiiiiiiiiiiiiii aiii'''
# findall,search,split,sub,finditer
# print(r"\n") for row string find isme ye \n print kar dega agar hum print("\n") karne se kewal spas dega new line ho jayega

#patt=re.compile(r'Tata')
#patt=re.compile(r'.st') # strint end with st 
#patt=re.compile(r'^Tata')
#patt=re.compile(r'01$')
# patt=re.compile(r'es*')
# patt=re.compile(r'es(2)*')
patt=re.compile(r'^91')
#patt=re.compile(r'{es}{1}')


matches=patt.finditer(mystr)
for match in matches:
    print(match)

