#https://www.codechef.com/COOK126C/problems/PASSWD


t=int(input())
for _ in range(t):
    s=str(input())
    countOfYes=0
    if len(s)>=10:
        countOfYes+=1
    for char in s:
        if ord(char) in range(97,123):
            countOfYes+=1
            break
        

    for i in range(1,len(s)-1):
        if ord(s[i]) in range(65,91):
            countOfYes+=1
            break
    for i in range(1,len(s)-1):    
        if s[i]=="0" or s[i]=="1" or s[i]=="2" or s[i]=="3" or s[i]=="4" or s[i]=="5" or s[i]=="6" or s[i]=="7" or s[i]=="8" or s[i]=="9":
            countOfYes+=1
            break
    for i in range(1,len(s)-1):
        if s[i] in ["@","#","%","&","?"]:
            countOfYes+=1
            break
    #print(countOfYes)
    if countOfYes==5:
        print("YES")
    else:
        print("NO")
    
