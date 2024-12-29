import random
computer=random.choice('RPS')
#print(computer)
print("R-Rock,P-paper,S-Scissor")
player=input("Enter your choice:")
if player in 'RPS':
    if computer==player:
        print("Tie")
    
    else:
    #palyer
        #if 'R'=='P' or 'P'=='S' or 'S'=='R':
        if (computer=='R' and player=='P') or (computer=='P' and player=='S') or(computer=='S' and player=='R'):
            print('---------Player is Win----------')
            print("Computer choice is:",computer)
        else:
            print('---------Computer is Win---------')
            print("Computer choice is:",computer)
else:
    print('Please enter valid data')
