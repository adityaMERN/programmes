t=int(input())
for _ in range(t):
    pc,pr=map(int,input().split(" "))
    strpc=len(str(pc))
    strpr=len(str(pr))
    if strpc==strpr and strpc==1:
        print(1,1)
    else:
        x=(pc%9+1)*(10**(pc//9))-1
        y= (pr%9+1)*(10**(pr//9))-1
        countofChef=len(str(x))
        countofR=len(str(y))
        if countofChef==countofR:
            print(1,countofR)
        elif countofChef>countofR:
            print(1,countofR)
        elif countofR>countofChef:
            print(0,countofChef)
