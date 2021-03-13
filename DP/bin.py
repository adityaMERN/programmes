A=3
num=str(bin(A).replace("0b", ""))
l=len(num)
left=32-l
s=("0"*left+num)[::-1]
print(s)
print(int(s,2))