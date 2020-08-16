class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        dp = grid
        m = len(dp)
        n = len(dp[0])

        for i in range(m-2,-1,-1):
            dp[i][n-1] += dp[i+1][n-1]

        for i in range(n-2,-1,-1):
            dp[m-1][i] += dp[m-1][i+1]

        for i in range(m-2,-1,-1):
            for j in range(n-2,-1,-1):
                dp[i][j] += min(dp[i+1][j],dp[i][j+1])

        return dp[0][0]