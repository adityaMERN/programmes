t=int(input())
for _ in range(t):
    n=int(input())
    if n<=30:
        print("NO")
    else:
        print("YES")
        if n in [36,40,44]:
            print(6,10,15,n-31)
        else:
            print(6,10,14,n-30)