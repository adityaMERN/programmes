#january long challenge codechef 2nd question
# 
# 
t=int(input())
for _ in range(t):
    n=int(input())
    s=str(input())
    alphabets=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p"]
    l=[]
    for i in range(0,n,4):
        inter=[]
        inter.append(s[i])
        inter.append(s[i+1])
        inter.append(s[i+2])
        inter.append(s[i+3])
        l.append(inter)
    #print(l)
    string=""
    for each in l:
        x="".join(each)
        #print(x)
        y=int(x,2)
        string+=alphabets[y]
    print(string)



         