class Solution:
	def isPlaindrome(self, S):
		# code here
		if len(S)==1:
		    return 1
        mid=len(S)//2
        high=len(S)-1
        low=0
        answer=0
        while low<mid:
            if S[low]==S[high]:
                high-=1
                low+=1
                answer=1
            else:
                answer=0
                break
        if answer==0:
            return 0
        else:
            return 1