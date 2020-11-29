t=int(input())
for _ in range(t):
    n=int(input())
    a=(n-1)//3
    sum3=(a*(3+a*3))//2
    b=(n-1)//5
    sum5=(b*(5+b*5))//2
    c=(n-1)//15
    sum15=(c*(15+c*15))//2
    summ=sum3+sum5-sum15
    print(summ)