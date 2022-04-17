class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """As Problem is related to find Unique Paths we need to store intial dp values as 1"""
        dp = [[1]*n for _ in range(m)]
        for i in range(1, m):
            for j in range(1, n):
                dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(m = 3, n = 7, Output = 28),
            dict(m = 7, n = 3, Output = 28),
            dict(m = 3, n = 3, Output = 6)]
    for test in tests:
        assert sol.uniquePaths(test['m'], test['n']) == test['Output']
        print("-----------------------------------------------------")