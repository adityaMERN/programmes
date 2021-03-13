#link: https://www.codechef.com/MARCH21B/problems/SPACEARR

t=int(input())
for _ in range(t):
    n=int(input())
    l=list(map(int,input().split(" ")))
    l.sort()
    indexList=[]
    for index,i in enumerate(l):
        x=index+1
        indexList.append([x,i])
    #print(indexList)
    summ=0
    flag=0
    for each in indexList:
        if each[1]>each[0]:
            flag=1
            break
        else:
            summ+=(each[0]-each[1])
    if flag==1:
        print("Second")
    elif flag==0 and summ%2!=0:
        print("First")
    else:
        print("Second")
