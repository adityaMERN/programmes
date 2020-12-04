t =int(input())
for _ in range(t):
    n= int(input())
    fib3 = 2
    fib6 = 0
    result = 2
    summed = 0
    while (result < n):
        summed += result;
        result = 4*fib3 + fib6
        fib6 = fib3
        fib3 = result
    print(summed)