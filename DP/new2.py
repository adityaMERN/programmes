
def solution(s):
    n=len(s)
    l=list(s)
    x=sorted(l)
#print(l)
#print(x)
    if l==x:
        return True
    else:
        return False
