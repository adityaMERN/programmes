t=int(input())
for _ in range(t):
    l=[]
    countOfx=0
    countOfo=0
    countOf_=0
    for i in range(3):
        a=input()
        aa=a[0]
        ab=a[1]
        ac=a[2]
        l.append([aa,ab,ac])
    for i in range(3):
        for j in range(3):
            if l[i][j]=="X":
                countOfx+=1
            elif l[i][j]=="O":
                countOfo+=1
            elif l[i][j]=="_":
                countOf_+=1
    XX=0
    OO=0
    if l[0][0]=="X" and l[0][1]=="X" and l[0][2]=="X":
        XX=1
    if l[1][0]=="X" and l[1][1]=="X" and l[1][2]=="X":
        XX=1
    if l[2][0]=="X" and l[2][1]=="X" and l[2][2]=="X":
        XX=1
    if l[0][0]=="X" and l[1][0]=="X" and l[2][0]=="X":
        XX=1
    if l[0][1]=="X" and l[1][1]=="X" and l[2][1]=="X":
        XX=1
    if l[0][2]=="X" and l[1][2]=="X" and l[2][2]=="X":
        XX=1
    if l[0][0]=="X" and l[1][1]=="X" and l[2][2]=="X":
        XX=1
    if l[0][2]=="X" and l[1][1]=="X" and l[2][0]=="X":
        XX=1
    

    if l[0][0]=="O" and l[0][1]=="O" and l[0][2]=="O":
        OO=1
    if l[1][0]=="O" and l[1][1]=="O" and l[1][2]=="O":
        OO=1
    if l[2][0]=="O" and l[2][1]=="O" and l[2][2]=="O":
        OO=1
    if l[0][0]=="O" and l[1][0]=="O" and l[2][0]=="O":
        OO=1
    if l[0][1]=="O" and l[1][1]=="O" and l[2][1]=="O":
        OO=1
    if l[0][2]=="O" and l[1][2]=="O" and l[2][2]=="O":
        OO=1
    if l[0][0]=="O" and l[1][1]=="O" and l[2][2]=="O":
        OO=1
    if l[0][2]=="O" and l[1][1]=="O" and l[2][0]=="O":
        OO=1
    if (XX==1 and OO==1) or (countOfx-countOfo<0) or(countOfx-countOfo>1):
        print(3)
    elif countOfx==0 and countOfo==0 and countOf_==9:
        print(2)
    elif XX==1 and OO==0 and countOfx>countOfo:
        print(1)
    elif XX==0 and OO==1 and countOfx==countOfo:
        print(1)
    elif XX==0 and OO==0 and countOf_==0:
        print(1)
    elif XX==0 and OO==0 and countOf_>0:
        print(2)
    else:
        print(3)
    