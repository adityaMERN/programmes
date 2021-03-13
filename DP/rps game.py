import random
n=int(input("Enter the number of chances:\n"))
computer=0
user=0
for i in range(n):
    x=random.choice(("ROCK","PAPER","SCISSORS"))
    k=int(input("Enter 1 for ROCK,2 for PAPER,3 for SCISSORS\n"))
    print(x)
    if k>3:
        print("Choose Wisely")
    elif k==1:
        if x=="PAPER":
            computer+=1
        elif x=="SCISSORS":
            user+=1
        else:
            print("same,so the round is tied\n")
    elif k==2:
        if x=="ROCK":
            user+=1
        elif x=="PAPER":
            print("same,so the round is tied\n")
        else:
            computer+=1
    elif k==3:
        if x=="ROCK":
            computer+=1
        elif x=="PAPER":
            user+=1
        else:
            print("same,so the round is tied")
    
if computer>user:
    print("The computer wins and the final score is",computer,":",user)
elif computer<user:
    print("The user wins and the final score is",user,":",computer)
else:
        print("Game Tied",user,":",computer)
print("Thank You For Playing")


