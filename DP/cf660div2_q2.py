t=int(input())
for _ in range(t):
    n=int(input())
    #length=len(str(n))
    x=(3*n)
    string=""
    for i in range(x//4):
        string+="9"
    for j in range(n-x//4):
        string+="8"
    print(string)