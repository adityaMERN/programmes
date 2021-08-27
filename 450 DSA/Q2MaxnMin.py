#https://www.geeksforgeeks.org/maximum-and-minimum-in-an-array/
l=list(map(int,input().split(" ")))
for i in range(len(l)-2):
    a=l[i]
    b=l[i+1]
    if a<=b:
        maximum=b
        minimum=a
    else:
        if a>maximum:
            maximum=a
            
        minimum=b
print(maximum,minimum)
