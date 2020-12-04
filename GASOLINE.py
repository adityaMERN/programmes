t=int(input())
for _ in range(t):
    n=int(input())
    fuel=list(map(int,input().split(" ")))
    cost=list(map(int,input().split(" ")))
    sortedCost=[item[0] for item in sorted(enumerate(cost),key=lambda item:item[1])]
    distance=n
    answer=0
    for car in sortedCost:
        carDistance=min(fuel[car],distance)
        distance-=carDistance
        answer+=carDistance*cost[car]
        if distance==0:
            break
    print(answer)