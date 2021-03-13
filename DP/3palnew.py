s=str(input())
ans=[]
i=0
for j in range(1,len(s)-2):
        string=s[i:j]
        if string==string[::-1]:
            ans.append(string)
print(ans)