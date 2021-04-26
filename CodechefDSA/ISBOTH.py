n=int(input())
if n%55==0:
    print("BOTH")
elif n%5==0:
    print("ONE")
elif n%11==0:
    print("ONE")
else:
    print("NONE")