class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels=['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        first=s[:len(s)//2]
        second=s[len(s)//2:]
        count1=0
        count2=0
        for char in first:
            if char in vowels:
                count1+=1
        for char in second:
            if char in vowels:
                count2+=1
        if count1==count2:
            return True
        else:
            return False
        
        