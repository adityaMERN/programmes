def ans(a,b,r,c):
    for i in range(r):
        for j in range(c):
            if a[i][j]!=b[i][j]:
                return False
    return True

t=int(input())
for _ in range(t):
    r,c,x=map(int,input().split(" "))
    a=[]
    b=[]
    for _ in range(r):
        rowA=list(map(int,input().split(" ")))
        a.append(rowA)
    for _ in range(r):
        rowB=list(map(int,input().split(" ")))
        b.append(rowB)
    if r<x and c<x:
        if a==b:
            print("Yes")
        else:
            print("N0")
    elif r<x:
        for i in range(r):
            for j in range((c-x+1)):
                if a[i][j]==b[i][j]:
                    continue
                else:
                    diff=b[i][j]-a[i][j]
                    a[i][j]+=diff
                    k=1
                    while k<x:
                        a[i][j+k]+=diff
                        k+=1
        if a==b:
            print("Yes")
        else:
            print("No")
    elif c<x:
        for i in range(c):
            for j in range(r-x+1):
                if a[j][i]==b[j][i]:
                    continue
                else:
                    diff=b[j][i]=a[j][i]
                    a[j][i]+=diff
                    k=1
                    while k<x:
                        a[j+k][i]+=diff
                        k+=1
        if a==b:
            print("Yes")
        else:
            print("No")
    elif c>=x and r>=x:
        for i in range(r):
            for j in range(c-x+1):
                if a[i][j]==b[i][j]:
                    continue
                else:
                    diff=b[i][j]-a[i][j]
                    a[i][j]+=diff
                    k=1
                    while k<x:
                        a[i][j+k]+=diff
                        k+=1
        for i in range(c):
            for j in range(r-x+1):
                if a[j][i]==b[j][i]:
                    continue
                else:
                    diff=b[j][i]=a[j][i]
                    a[j][i]+=diff
                    k=1
                    while k<x:
                        a[j+k][i]+=diff
                        k+=1
        if a==b:
            print("Yes")
        else:
            print("No")




# 3
# 2 2 2
# 1 2
# 0 1
# 0 0
# 0 0
# 2 2 2
# 1 2
# 0 1
# 0 0
# -1 0
# 3 2 2
# 1 1
# 2 2
# 3 3
# 1 0
# 2 0
# 3 0




