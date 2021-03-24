#https://www.codechef.com/COOK127B/problems/MATXOR
# Explanation: If we have n as even number then we will iterate in n and if i is odd we take the first element of the row and last element 
# from the nextrow. If n is odd we do same for the n-1 rows and in the last row we take xor of each element in final answer.


t=int(input())
for _ in range(t):
    n,m,k=map(int,input().split(" "))
    # l=[]
    # for i in range(1,n+1):
    #     row=[]
    #     for j in range(1,m+1):
    #         row.append(k+i+j)
    #     l.append(row)
    # output=0
    # for i in range(n):
    #     for j in range(m):
    #         output^=l[i][j]
    # print(output)
    answer=0
    if n%2==0:
        for i in range(1,n+1,2):
            x=k+i+1
            y=k+i+1+m
            intermediate=x^y
            answer=answer^intermediate
    else:
        for i in range(1,n,2):
            x=k+i+1
            y=k+i+1+m
            intermediate=x^y
            answer=answer^intermediate
        for each in range(1,m+1):
            new=k+n+each
            answer=answer^new
    print(answer)



