#january long challenge codechef 3rd question

t=int(input())
for _ in range(t):
    n,m=map(int,input().split(" "))
    john=list(map(int,input().split(" ")))
    jack=list(map(int,input().split(" ")))
    sumJohn=sum(john)
    sumJack=sum(jack)
    if sumJohn>sumJack:
        print("0")
    else:
        count=0
        for i in range(n):
            john.sort()
            jack.sort()
            x=john[0]
            y=jack[-1]
            if x<y:
                temp=x
                john[0]=y
                jack[-1]=temp
                count+=1
                if sum(john)>sum(jack):
                    break
                else:
                    if i!=n-1:
                        continue
                    else:
                        count=-1
            else:
                count=-1
        print(count)
        

