#january circuit 2021
#hackerearth question #2
def lcm(n1,n2):
    if n1>n2:
        nums=n1
        denominator=n2
    else:
        nums=n2
        denominator=n1
    reminder=nums%denominator
    while(reminder!=0):
        nums=denominator
        denominator=reminder
        reminder=nums%denominator
    greatest=denominator
    least=int(int(n1*n2)/int(greatest))
    return least
t=int(input())
for _ in range(t):
    n=int(input())
    print(n*(n+1)//2,end=" ")
    L=[]
    for i in range(1,n+1):
        L.append(i)
    least=L[0]
    if n>=2:
        num=L[1]
        if(least>num):
            nums=least
            denominator=num
        else:
            nums=num
            denominator=least
        reminder=nums%denominator
        while(reminder!=0):
            nums=denominator
            denominator=reminder
            reminder=nums%denominator
        greatest=denominator
        least=int(int(least*num)/int(greatest))
    for i in range(2,len(L)):
        least=lcm(least,L[i])
        if(least>L[i]):
            nums=least
            denominator=L[i]
        else:
            nums=L[i]
            denominator=least
        reminder=nums%denominator
        while(reminder!=0):
            nums=denominator
            denominator=reminder
            reminder=nums%denominator
        greatest=denominator
        least=int(int(least*L[i])/int(greatest))
    print(least)

