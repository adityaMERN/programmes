version1=str(input())
version2=str(input())
a=version1.split(".")
b=version2.split(".")
#lena=len(a)
#lenb=len(b)
while len(a)<len(b):
    a.append("0")
while len(b)<len(a):
    b.append("0")
print(a)
print(b)
similar=0
ver1=0
ver2=0
for i in range(len(a)):
    if int(a[i])>int(b[i]):
        print("1")
        break
    if int(a[i])<int(b[i]):
        print("-1")
        break
    else:
        similar+=1
if similar==len(a):
    print(0)