import random      #Random Function
print("WELCOME TO HANGMAN")
print("\n START GUESSING")
word=['gamer','tree','mobile','computer','keyboard','railways','aeroplane','tiger','spider','rabbit','laptop','drawing' ] #random words
w=random.choice(word)      # picks the random word
g=''    # guess
t=7     #Turn
while t>0:
    f=0     #Failing
    for i in w:
        if i in g:
            print(i,end=' ')   #printing Word
        else:
            print('_',end=' ') #printing space
            f=f+1
    if f==0:           #if fail = 0
        print("WINNER")
    a=input("\n guess the character= ")# guess the character
    g=g+a
    if a not in w:
        t=t-1      # decreasing turn
        if t==6:
            print("wrong Guess")
            print("NEXT TURN")
            print("------- ")
            print("|     | ")
            print("|       ")
            print("|       ")
            print("|       ")
        elif t==5:
            print("wrong Guess")
            print("NEXT TURN")
            print("-------  ")
            print("|     |  ")
            print("|     0  ")
            print("|        ")
            print("|        ")
        elif t==4:
            print("wrong Guess")
            print("NEXT TURN")
            print("-------  ")
            print("|     |  ")
            print("|     0  ")
            print("|    /    ")
            print("|        ")
        elif t==3:
            print("wrong Guess")
            print("NEXT TURN")
            print("-------  ")
            print("|     |  ")
            print("|     0  ")
            print("|    /|   ")
            print("|        ")
        elif t==2:
            print("wrong Guess")
            print("NEXT TURN")
            print("-------  ")
            print("|     |  ")
            print("|     0  ")
            print("|    /|\   ")
            print("|        ")
        elif t==1:
            print("wrong Guess")
            print("NEXT TURN")
            print("-------  ")
            print("|     |  ")
            print("|     0  ")
            print("|    /|\   ")
            print("|    /    ")
        else:
            print("LOOSER")
            print("-------  ")
            print("|     |  ")
            print("|     0  ")
            print("|    /|\   ")
            print("|    / \   ")
            print("TRY AGAIN")
