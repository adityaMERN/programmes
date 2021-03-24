#find product using recursion

def add(n,n1,n2):
   if n==n2:
       return n1
   else:
        return n1+add(n+1,n1,n2)
n1=int(input())  #5
n2=int(input()) 
n=1
if (n1<0 and n2<0) :
       n1=-1*n1
       n2=-1*n2
       x=add(n,n1,n2)
       print(x)
elif (n1>0 and n2>0):
       x=add(n,n1,n2)
       print(x)
elif n1==0 or n2==0:
      print("0")
elif n1<0 or n2<0:
    if n1<0:
        n1=-1*n1
        x=add(n,n1,n2)
        res=(-1)*x
        print(res)
    elif n2<0:
        n2=-1*n1
        x=add(n,n1,n2)
        res=(-1)*x
        print(res)