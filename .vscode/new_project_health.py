
from ast import Compare
from pygame import init, mixer
from datetime import datetime
from time import time
def musiconloop(file,stoper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.set_volume(0.2)
    mixer.music.play()
    while True:
        a=input()
        if a==stoper:
            mixer.music.stop()
            break  
        
def log_file(msg):
       with open("log.txt","a") as f:
                  f.write(f"{msg},{datetime.now()}\n")              
if __name__=='__main__':
     #musiconloop('D:\PythonProject\pytitorial\.vscode\exame\water.mp3','stoper')
     init_water=time()
     init_eyes=time()
     init_exersize=time()
     waterSec=20
     eyesSec=30
     exersizesec=45
     
     while True:
        if time()-init_water>waterSec:
            print("Water Drinking time,Enter'Drank' stop the alarm ")
            musiconloop('D:\PythonProject\pytitorial\.vscode\exame\water.mp3','Drank')
            init_water=time()
            log_file("Water Drink complite")
        if time()-init_eyes>eyesSec:
                print("Eyes refrece time,Enter'Wash' stop the alarm ")
                musiconloop('D:\PythonProject\pytitorial\.vscode\exame\water.mp3','Wash')
                init_eyes=time()
                log_file('refrece Eye at')
        if time()-init_exersize>exersizesec:
                  print("Phisical Exersize time,Enter'Comp' stop the alarm ")
                  musiconloop('D:\PythonProject\pytitorial\.vscode\exame\water.mp3','Comp')
                  init_exersize=time()
                  log_file('Phisical Exersize complite at')          
                
                        
                     
                  
                  
     
 
 


        
        
        