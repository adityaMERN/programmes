# https://codingcompetitions.withgoogle.com/kickstart/round/0000000000436140/000000000068cca3#problem

t=int(input())
for _ in range(t):
    n,k=map(int,input().split(" "))
    s=str(input())
    #minop=0
    x=0
    for i in range(len(s)//2):
        if s[i]!=s[len(s)-i-1]:
            x+=1
    if x==k:
        print("0")
    elif x>k:
        print(x-k)
    else:
        print(k-x)