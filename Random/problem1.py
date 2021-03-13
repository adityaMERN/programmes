t=int(input())
for _ in range(t):
    n=int(input())
    def funInverse(x):
        rev = 0
        while(x > 0): 
            a = x % 10
            rev = rev * 10 + a 
            x = x // 10
        return rev
    middle=funInverse(n)
    #print(middle)
    upper=funInverse(middle)
    #print(upper)
    print(len(str(upper)))
        