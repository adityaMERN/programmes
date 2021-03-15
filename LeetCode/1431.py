class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        maximum=max(candies)
        final=[]
        for i in candies:
            final.append((i+extraCandies)>=maximum)
        return final