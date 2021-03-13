arr=list(map(int,input().split(" ")))
summ=int(input())
def subset(arr,summ):
    #t=[len(arr)+1][summ+1]
    t=[[False for j in range(summ+1)] for i in range(len(arr)+1)]
    for i in range(len(arr)+1):
        for j in range(summ+1):
            if i==0:
                t[i][j]=False
            elif j==0:
                t[i][j]=True
            else:
                if arr[i-1]<=j:
                    t[i][j]=t[i-1][j-arr[i-1]] or t[i-1][j]
                else:
                    t[i][j]=t[i-1][j]   
    return t[len(arr)][summ]
if subset(arr,summ)==True:
    print("True")
else:
    print("False")       
