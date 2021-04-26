# https://practice.geeksforgeeks.org/problems/smallest-divisible-number/1/?track=dsa-workshop-1-mathematics&batchId=308


def getSmallestDivNum(self, n): 
        def gcd(a,b):
            if a == 0:
                return b
           
            return gcd(b % a, a)
            
        # code here 
        y=2 
        for i in range(1,n+1,2):
            x=i
            if x>y:
                ans=(x*y)//gcd(x,y)
            else:
                ans=(x*y)//gcd(y,x)
            y=ans
        return ans