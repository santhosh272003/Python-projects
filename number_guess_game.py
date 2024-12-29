import random
#computer
computer=random.randint(0,9)
#print(computer)
#player
user=int(input("Enter your number:"))
if user==computer:
    print("------Congrats-------")
else:
    if computer<user:
        print("-------Original number is lesser than you number--------")
        print(f"____computer generated num is:{computer}____")
    elif computer > user:
        print("-------Original number is Greater than your number--------")
        print(f"___computer generated num is:{computer}___")
        

