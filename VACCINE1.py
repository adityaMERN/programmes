d1,v1,d2,v2,p=map(int,input().split(" "))
summ=0
f=0
if d1<d2:
    day=d1-1
    while summ<p:
        summ+=v1
        if d1==d2 or f==1:
            summ+=v2
            f=1
        d1+=1
        day+=1
    print(day)
else:
    day=d2-1
    while summ<p:
        summ+=v2
        if d1==d2 or f==1:
            summ+=v1
            f=1
        d2+=1
        day+=1
    print(day)




    #https://www.codechef.com/DEC20B?order=desc&sortBy=successful_submissions
