n=int(input())
num=list(map(int,input().split(" ")))
binary=[]
for i in num:
    binary.append(bin(i).replace("0b", ""))
binary.sort(key=len,reverse=True)
#print(binary)
x=len(binary[0])
#print(x)
for i in range(len(binary)):
    binary[i]=("0"*(x-len(binary[i])))+binary[i]
#print(binary)
new=[]
c=0
total0=0
total1=0
for k in binary:
    countOf0=str(k).count("0")
    countOf1=str(k).count("1")
    new.append([countOf0,countOf1])
    total0+=countOf0
    total1+=countOf1
for i in range(len(new)-1):
    for j in range(i+1,len(new)):
        intermediate=new[i:j]

        







