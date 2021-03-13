def solution(n):
    for i in range(1,n+1):
        if i%2==0 and i%3==0 and i%5==0:
            print("CodilityTestCoders")
        elif i%2 ==0 and i%3==0:
            print("CodilityTest")
        elif i%2==0 and i%5==0:
            print("CodilityCoders")
        elif i%3==0 and i%5==0:
            print("TestCoders")
        elif i%2==0:
            print("Codility")
        elif i%3==0:
            print("Test")
        elif i%5==0:
            print("Coders")
        else:
            print(i) 