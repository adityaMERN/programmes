def print1(arr):
    n = len(arr)
    indices = [0 for i in range(n)]
 
    while (1):
        for i in range(n):
            print(arr[i][indices[i]], end = " ")
        print()
        next = n - 1
        while (next >= 0 and
              (indices[next] + 1 >= len(arr[next]))):
            next-=1
        if (next < 0):
            break
        indices[next] += 1
        for i in range(next + 1, n):
            indices[i] = 0


def letterCombinations( digits):
    combination=[["a","b","c"],["d","e","f"],["g","h","i"],["j","k","l"],["m","n","o"],["p","q","r","s"],["t","u","v"],["w","x","y","z"]]
    l=[]
    for each in digits:
        l.append(combination[int(each)-2])
    y=print1(l)
    return y
    
    
    
digits=str(input())
x=letterCombinations(digits)
print(x)          
        