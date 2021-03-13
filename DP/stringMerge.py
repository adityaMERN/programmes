m_bits=256  
def compare(arr1, arr2):
    for i in range(m_bits): 
        if arr1[i] != arr2[i]: 
            return False
    return True  
def search(pat, txt1): 
    l=[]
    for txt in txt1:
        M = len(pat) 
        N = len(txt) 
        countP = [0]*m_bits

        countTW = [0]*m_bits

        for i in range(M): 
            (countP[ord(pat[i]) ]) += 1
            (countTW[ord(txt[i]) ]) += 1

        for i in range(M,N): 
            if compare(countP, countTW): 
                #print("Found at Index", (i-M))
                index=i-M
                l.append(txt[0:index]+txt[index+len(pat):])

            (countTW[ ord(txt[i]) ]) += 1

            (countTW[ ord(txt[i-M]) ]) -= 1
 
        if compare(countP, countTW): 
            #print("Found at Index", N-M) 
            index=N-M
            #print("here")
            l.append(txt[0:index]+txt[index+len(pat):])

    return l



s=str(input())
n=int(input())
l=[]
for i in range(n):
    l.append(str(input()))
#l=["luk","pid"]

out=[]
out.append(ful)
for i in l:
    out=search(i,out)
   
out.sort()

if len(out)==0:
    print("NO")
elif out[0]=="":
    print("YES")
else:
    print("NO")
