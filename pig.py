#roll a die, number 1-6 , add that to your score, score goes to zero if you get 1 on your dice, 
#you decide how many times do you wanna play, max score is 50

from random import *
sum = [0,0,0,0,0]
#sum = [ 0 for _ in range(n) ]

def roll():
    print ("\n Rolling the dice for player ", i)
    print ("......\n")
    choi = randint(1,6)
    print ("the number on the dice is " ,choi)
    if choi != 1:
        sum [i-1] = sum [i-1] + choi
        print("your score is ", sum[i-1])
        if sum[i-1] >= 20:
            print("congrats, player " + str(i) + " has won")
            quit()
        else:
            choice = input("\nDo you still want to roll or pass\n").lower()
            if choice == "roll":
                roll()
            elif choice == "pass":
                main()
            else:
                quit()
    elif choi == 1:
        sum[i-1] = 0
        print ("\n OOPS, your score is back to 0 \n")
        main()
i = 0 

def main():
    global i
    if i == n:
        i = 0
    for i in range(i+1,n+1):
        choice = input("\nPlayer " +  str(i) + " choose roll or pass \n").lower()
        if choice == "roll":
            roll()
        elif choice == "pass":
            continue
        else:
            quit()

while True:
        n = int(input("Enter number of players(2-4) \n"))
        if (n>4 or n<2):
            print("Enter a valid number ")
            continue
        else:
             main()       




