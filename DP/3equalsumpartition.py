arr=list(map(int,input().split(" ")))
n=len(arr)
s=sum(arr)
if s%2!=0:
   # print("1")
    print("False")
else:
    summ=s//2
    def equal_sum(arr,summ):
        t=[[False for j in range(summ+1)]for i in range(n+1)]
        #print(summ)
        for i in range(n+1):
            for j in range(summ+1):
                if j==0:
                    t[i][j]=True
                elif i==0:
                    t[i][j]=False
                else:
                    if arr[i-1]<=j:
                        t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
                    else:
                        t[i][j]=t[i-1][j]
        print(t)
        return t[n][summ]
#print(t)
    if equal_sum(arr,summ)==True:
        #print("2")
        print("True")
    else:
        #print("3")
        print("False")