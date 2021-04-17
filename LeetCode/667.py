class Solution:
    def constructArray(self, n: int, k: int) -> List[int]:
        
        solution = [1]
        offset = k
        currentSign = 1
        
        while abs(offset) >= 1:
            if currentSign == 1:
                solution.append(solution[-1] + offset)
                currentSign = 0
            else:
                solution.append(solution[-1] - offset)
                currentSign = 1
            offset -= 1
        
        for i in range(1, n+1):
            if i not in solution:
                solution.append(i)
        
        return solution