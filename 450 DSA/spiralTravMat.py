#https://practice.geeksforgeeks.org/problems/spirally-traversing-a-matrix-1587115621/1
class Solution:
    def spiralOrder(self, A: List[List[int]]) -> List[int]:
        final=[]
        m=len(A)
        if m==0:
            return []
        
        else:
            n=len(A[0])
            top=0
            right=n-1
            left=0
            bottom=m-1
            direction=0
            while left<=right and top<=bottom :
                if direction==0:
                    for i in range(left,right+1):
                        final.append(A[top][i])
                    top+=1
                    direction=1
                elif direction==1:
                    for i in range(top,bottom+1):
                        final.append(A[i][right])
                    right-=1
                    direction=2
                elif direction==2:
                    for i in range(right,left-1,-1):
                        final.append(A[bottom][i])
                    bottom-=1
                    direction=3
                elif direction==3:
                    for i in range(bottom,top-1,-1):
                        final.append(A[i][left])
                    left+=1
                    direction=0
        return final

        