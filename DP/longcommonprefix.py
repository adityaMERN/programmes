A=list(map(str,input().split(" ")))
length=len(A)
if length==0:
    print("")
elif length==1:
    print(A[0])
A.sort()
i=0
minimum=min(len(A[0]),len(A[length-1]))
while (i<minimum and A[0][i]==A[length-1][i]):
    i+=1
prefix=A[0][:i]
print(prefix)