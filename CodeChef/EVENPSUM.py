t=int(input())
for _ in range(t):
    a,b=map(str,input().split(" "))
    if a==1 or b==1:
        print(1)
    else:
        x=int(a)*int(b)
        if x%2==0:
            print(x//2)
        else:
            print(x//2+1)

#Link: https://discuss.codechef.com/t/evenpsum-editorial/81932
#December long challenge 2020