class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        # def countSubsquare(arr, n,m, X):
        #     m=len(arr[0]) 
        #     dp = [[ 0 for x in range(m + 1)]
        #       for y in range(n + 1)]
        #     for i in range(n):
        #         for j in range(m):
        #             dp[i + 1][j + 1] = arr[i][j]
        #     for i in range(1, n + 1):
        #         for j in range(1, m + 1):
        #             dp[i][j] += (dp[i - 1][j] + 
        #                  dp[i][j - 1] - 
        #                  dp[i - 1][j - 1])
        #     cnt = 0
        #     for i in range(1, n + 1):
        #         for j in range(1, m + 1):
        #             lo = 1
        #             hi = min(n - i, m - j) + 1
        #             found = False
        #             while (lo <= hi):
        #                 mid = (lo + hi) // 2
        #                 ni = i + mid - 1
        #                 nj = j + mid - 1
        #                 summ = (dp[ni][nj] - dp[ni][j - 1] - dp[i - 1][nj] + dp[i - 1][j - 1])
        #                 if (summ >= X):
        #                     if (summ == X):
        #                         found = True
        #                     hi = mid - 1
        #                 else:
        #                     lo = mid + 1
        #             if (found == True):
        #                 cnt += 1
        #     return cnt
        # x=countSubsquare(matrix,len(matrix),len(matrix[0]),target)
        # return x
        xlen, ylen, ans = len(matrix[0]), len(matrix), 0
        
        for r in matrix:
            for j in range(1, xlen):
                r[j] += r[j-1]
        for j in range(xlen):
            for k in range(j, xlen):
                res, csum = {0: 1}, 0
                for r in matrix:
                    csum += r[k] - (r[j-1] if j else 0)
                    if csum - target in res: ans += res[csum-target]
                    res[csum] = res[csum] + 1 if csum in res else 1  
        return ans