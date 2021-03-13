n=int(input())
b=str(input())
g=str(input())
bride=[]
groom=[]
for k in range(n):
    bride.append(b[k])
    groom.append(g[k])
#print(bride)
#print(groom)
#i=0
#groom.append(groom.pop(0))
i=0
while n>=0:
    if bride[0]==groom[0]:
        bride.pop(0)
        groom.pop(0)
        n-=1
        if len(bride)==0:
            print("0")
    else:
        groom.append(groom.pop(0))
        #n=len(groom)
        if bride[0] not in groom:
            print(len(groom))
            break
        else:
            n=len(groom)

        



                

