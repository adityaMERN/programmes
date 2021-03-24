#Write a program to reverse an array or string


#if list
a=list(map(int,input().split(" ")))
output=[]
for i in range(len(a)-1,-1,-1):
     output.append(a[i])
print(output)
# x=a[::-1]
# print(x)



# #if string:
s=str(input())
l=list(s)
output=""
for i in range(len(l)-1,-1,-1):
    output+=l[i]
print(output)
