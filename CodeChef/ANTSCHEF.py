#january long challenge codechef 6th question

t=int(input())
for _ in range(t):
    n=int(input())
    collison=0
    if n==1:
        for each in range(n):
            m=list(map(int,input().split(" ")))
            x=m[0]
            cpos=0
            cneg=0
            for i in range(1,x+1):
                if m[i]>0:
                
                    cpos+=1
                else:
                
                    cneg+=1
    collison+=(cpos*cneg)
    print(collison)
