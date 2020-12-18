t=int(input())
for _ in range(t):
    n,k=map(int,input().split(" "))
    arr=[]
    if n==k:
        print(" ".join(str(i+1) for i in range(n)))
    else:
        if n%2==0:
            count=n//2
            for i in range(1,n+1):
                if i%2!=0:
                    x=i*(-1)
                    arr.append(x)
                else:
                    arr.append(i)
        else:
            count=n//2+1
            for i in range(1,n+1):
                if i%2==0:
                    x=i*(-1)
                    arr.append(x)
                else:
                    arr.append(i)
        #print(a)
        summ=1
        diff=0
        for i in range(1,n):
            summ+=arr[i]
            if summ>0:
                if count<k:
                    diff=k-count
                    for j in range(n-1,0,-1):
                        if arr[j]<0:
                            arr[j]=arr[j]*-1
                            count+=1
                            if count==k:
                                break
                elif count>k:
                    diff=count-k
                    for j in range(n-1,0,-1):
                        if arr[j]>0:
                            arr[j]=arr[j]*-1
                            count-=1
                            if count==k:
                                break
        print(" ".join(str(arr[i]) for i in range(n)))                 







#https://www.codechef.com/DEC20B?order=desc&sortBy=successful_submissions











