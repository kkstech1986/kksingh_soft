
from pygame import mixer
def musiconloop(file,stoper):
    mixer.init()
    mixer.music.load(file)
    mixer.music.play()
    while True:
        a=input()
        if a==stoper:
            mixer.music.stop()
            break
        
if __name__=='__main__':
 musiconloop("D:\PythonProject\pytitorial\.vscode\exame\water.mp3","stoper")
 