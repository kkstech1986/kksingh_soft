#lac 61
class GrandFather():
     
     def lang():
         language=10
         print(f"very nice  sing a song in {language}")
class Father(GrandFather):
     
    def playing():
        play="Gitar"
        print(f"very nice play a {play}")    
class son(Father):
    
    def dancing():
         dance=10
         print(f"very nice dance in stap {dance}")    

s=son
f=Father 
g=GrandFather
g.lang()
s.lang()
f.lang()
