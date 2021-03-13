k=int(input())
num=0
for i in range(k+1):
    num=(num*10+7)%k
    if num==0:
        print(i+1)
        break
if num:
    print("-1")