s=str(input())
n=len(s)
dp=[[False for i in range(n)] for j in range(n)]
for i in range(n):
    dp[i][i]=1
for l in range(2,n+1):
    for i in range(n-l+1):
        j=i+l-1
        if l==2:
            if s[i]==s[j]:
                dp[i][j]=1
        else:
            if s[i]==s[j] and dp[i+1][j-1]:
                dp[i][j]=0
print(dp)
ans=[]
for i in range(n-2):
    if dp[0][i]:
        for j in range(i+1,n-1):
            if dp[i+1][j] and dp[j+1][n-1]:
                ans.append(s[0:(i+1)])
                ans.append(s[(i+1):(j-1)])
                ans.append(s[(j+1):(n-j)])
print(ans)
if len(ans)==0:
    print("Impossible")
else:
    for words in ans:
        print(words)