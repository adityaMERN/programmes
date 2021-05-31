matrix=[[0 for i in range(1001)] for j in range(1001)]
    #print(matrix)
for i in range(1,1001):
    matrix[i][1]=((i)*(i+1))//2
    
    for j in range(2,1001):
        matrix[i][j]=matrix[i][j-1]+j-1+i-1
t=int(input())
for _ in range(t):
    x1,y1,x2,y2=map(int,input().split(" "))
    
            
    summ=0
    for i in range(x1,x2+1):
        #print(matrix[i][y1-1])
        summ+=matrix[i][y1]
    #print("\n")
    for j in range(y1+1,y2+1):
        #print(matrix[x2-1][j])
        summ+=matrix[x2][j]
    #print("\n")
    print(summ)