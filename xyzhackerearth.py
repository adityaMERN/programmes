def row_sum(arr,n,m,l,r):
    rowSumMatrix=[]
    summ=0
    for i in range(n):
        for j in range(m):
            summ+=arr[i][j]
        if summ>=l and summ<=r:
            rowSumMatrix.append(summ)
        summ=0
    return rowSumMatrix
def column_sum(arr,n,m,l,r):
    columnSumMatrix=[]
    summ=0
    for i in range(n):
        for j in range(m):
            summ+=arr[j][i]
        if summ>=l and summ<=r:
            columnSumMatrix.append(summ)
        summ=0
    return columnSumMatrix
if __name__=="__main__":
    n=int(input())
    m=int(input())
    matrix=[]
    for _ in range(n):
        rows=list(map(int,input().split(" ")))
        matrix.append(rows)
    queries=int(input())
    s=int(input())
    querymatrix=[]
    for _ in range(queries):
        l,r=map(int,input().split(" "))
        count_row=0
        count_column=0
        x=row_sum(matrix,n,m,l,r)
        y=column_sum(matrix,n,m,l,r)
        length_x=len(x)
        length_y=len(y)
        querymatrix.append(length_x+length_y)
    for each in querymatrix:
        print(each,end= " ") 

