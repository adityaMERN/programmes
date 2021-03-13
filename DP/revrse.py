a=str(input())
b=a.strip()
l=b.split(" ")
print(l)
new=[]
for i in l:
    if i!="":
        new.append(i)
print(new)
print(" ".join(new[::-1]))