def ascending(A,low,high,B):
            while low<=high:
                mid=low+(high-low)//2
                if A[mid]==B:
                    return mid
                if A[mid]>B:
                    high=mid-1
                else:
                    low=mid+1
            return -1
def descending(A,low,high,B):
            while low<=high:
                mid=low+(high-low)//2
                if A[mid]==B:
                    return mid
                if A[mid]<B:
                    high=mid-1
                else:
                    low=mid+1
            return -1
def bitonic_index(A,low,high):
            #while l<=h:
                mid=low+(high-low)//2
                if A[mid]>A[mid-1] and A[mid]>A[mid+1]:
                    #print(mid)
                    return mid
                elif A[mid]>A[mid-1] and A[mid]<A[mid+1] :
                    return bitonic_index(A,mid,high)
                    #l=mid
                elif A[mid]<A[mid-1] and A[mid]>A[mid+1]:   
                    return bitonic_index(A,low,mid)
        #print(index)                   
def searchbitonic(A,n,B,found):
            if B>A[found]:
                return -1
            elif B==A[found]:
                return found
            else:
                temp=ascending(A,0,found-1,B)
                if(temp!=-1):
                    return temp
                return descending(A,found+1,n-1,B)
A=list(map(int,input().split(" ")))
B=int(input())
n=len(A)
l=0
h=n-1
index=bitonic_index(A,l,h)
x=searchbitonic(A,n,B,index)
print(x)