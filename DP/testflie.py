n=int(input())
m=int(input())
t=[]
for _ in range(n):
    horizontal=list(map(str,input().split(" ")))
    t.append(horizontal)
position=[]
for i in range(n):
    for j in range(m):
        if t[i][j]=="R":
            position.append((i,j))
            continue
        elif t[i][j]=="B":
            position.append((i,j))
            continue
        elif t[i][j]=="Q":
            position.append((i,j))
            continue
def r_movement(position[0]):
    left=0
    right=0
    up=0
    down=0
    for i in range(n):
        for j in range(m):
            #left
            x=position[0][1]-1
            if x>0:
                if x-1==0:
                    if t[i][0]==".":
                        left+=1
                else:
                    for k in range(position[0][1],-1,-1):
                        if t[i][k]==".":
                            left+=1
                        else:
                            break
            #right
            y=m-1-position[0][1]
            if y0:



    



