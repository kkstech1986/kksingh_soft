
# no of quesses 9
#print no of guessees left
# No of guesses he look to finish 
#game over
n=18
NoOfGuesses=10
i=9
while(i>=1):
    a=int(input("Enter a Guesses :" ))    
    if a==n:
        print ("Great You are winner")
        print(f"your total number of gesses {NoOfGuesses-i}")
        break
    elif a<18:   
        print("you Enter a smaller number")
        print(f"Number of Guesses you left {i-1}")
    elif a>18:
        print("You Enter Biger Number")
        print(f"Number of Guesses you left {i-1}")
    i=i-1
print("Game Over")          
        
   

