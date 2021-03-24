#   https://www.codechef.com/COOK127B/problems/GUESSIT



import sys
t=int(input())
for _ in range(t):
    for i in range(1,1001):
        print(i**2)
        ans=int(input())
        if ans==1:
            break
        elif ans==0:
            continue
        else:
            sys.exit()

