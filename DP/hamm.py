from itertools import combinations_with_replacement
def hammingDistance(A):
        summation=0
        if len(A)==1:
            return 0
        else:
            l=list(combinations_with_replacement(A, 2))
            new=[]
            for i in l:
                if i[0]!=i[1]:
                    new.append([i[1],i[0]])
            l=l+new
            print(l)
            for i in l:
                if i[0]==i[1]:
                    summation+=0
                else:
                    x1=str(bin(i[0])).replace("0b","")
        #print(x1)
                    x2=str(bin(i[1])).replace("0b","")
        #print(x2)
                    c=0
                    if len(x1)>len(x2):
                        bin2="0"*(len(x1)-len(x2))+x2
                        for k in range(len(bin2)):
                            if bin2[k]!=x1[k]:
                                c+=1
                    else:
                        bin1="0"*(len(x2)-len(x1))+x1
            #print(bin1)
                        for k in range(len(bin1)):
                            if bin1[k]!=x2[k]:
                                c+=1
                    summation+=c
        return summation%1000000007
A=[2,4,6]
x=hammingDistance(A)
print(x)
