#question link: https://www.codechef.com/START1B/problems/COUPON2

t=int(input())
for _ in range(t):
    d,c=map(int,input().split(" "))
    a1,a2,a3=map(int,input().split(" "))
    b1,b2,b3=map(int,input().split(" "))
    sum1st=a1+a2+a3
    sum2nd=b1+b2+b3
    #without coupon:
    sumPaidWithoutCoupon=sum1st+sum2nd+d+d
    if sum1st>=150 and sum2nd>=150:
        sumPaid=sum1st+sum2nd+c
    elif sum1st>=150 and sum2nd<150:
        sumPaid=sum1st+sum2nd+c+d
    elif sum1st<150 and sum2nd>=150:
        sumPaid=sum1st+d+sum2nd+c
    else:
        sumPaid=sum1st+sum2nd+2*d
    x=min(sumPaid,sumPaidWithoutCoupon)
    if x<sumPaidWithoutCoupon:
        print("YES")
    else:
        print("NO")