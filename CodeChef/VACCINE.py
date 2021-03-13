t=int(input())
for _ in range(t):
    n,d=map(int,input().split(" "))
    arr=list(map(int,input().split(" ")))
    serious=[]
    nonserious=[]
    for i in arr:
        if i>=80 or i<=9:
            serious.append(i)
        else:
            nonserious.append(i)
    days=0
    if len(serious) %d==0:
        seriousDays=len(serious)//d
    else:
        seriousDays=len(serious)//d+1
    if len(nonserious)%d==0:
        nonseriousdays=len(nonserious)//d
    else:
        nonseriousdays=len(nonserious)//d+1
    days=seriousDays+nonseriousdays
    print(days)
        
#https://www.codechef.com/DEC20B?order=desc&sortBy=successful_submissions