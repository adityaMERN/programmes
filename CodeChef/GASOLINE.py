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


# PROBLEM:
# There are nn cars on a circular track of length nn, the ii-th of them is on clockwise distance i-1i−1 from the car 11.

# You can fill the ii-th car with at most f_if 
# i
# ​	
#   litres of gasoline and pay c_ic 
# i
# ​	
#   coins for each litre. Then you choose one of the cars, and start driving clockwise, the car spends one litre of gasoline per unit of distance. When you pass through another car, you steal all its gasoline.

# Fill the cars with the minimum cost in such a way, that is possible to choose a car and travel a distance nn clockwise.