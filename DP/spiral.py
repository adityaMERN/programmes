def spiralOrder(A):
    final=[]
    m=len(A)
    if m==0:
        return []
    else:
        n=len(A[0])
            #eg:     top<-- 1  2  3
            #               4  5  6
            #      bottom<--7  8  9 -->right
            #              \|/
            #               left

        top=0
        right=n-1
        left=0
        bottom=m-1
        direction=0
    #defining directions
    #direction =0 means left to right
    #direction =1 means top to bottom
    #direction =2 means right to left
    #direction =3 means bottom to top
        while left<=right and top<=bottom :
            if direction==0:
                for i in range(left,right+1):
                    final.append(A[top][i])
                top+=1
                direction=1
            elif direction==1:
                for i in range(top,bottom+1):
                    final.append(A[i][right])
                right-=1
                direction=2
            elif direction==2:
                for i in range(right,left-1,-1):
                    final.append(A[bottom][i])
                bottom-=1
                direction=3
            elif direction==3:
                for i in range(bottom,top-1,-1):
                    final.append(A[i][left])
                left+=1
                direction=0
    return final
A=[]
m=int(input())
n=int(input())
for row in range(m):
    column=list(map(int,input().split(" ")))
    A.append(column)
x=spiralOrder(A)
print(x)