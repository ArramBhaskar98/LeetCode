class Solution:
	def uniquePathsWithObstacles(self, obstacleGrid):
		m = len(obstacleGrid)
		n = len(obstacleGrid[0])
		dp = [[0]*n for _ in range(m)]
		dp[m-1][n-1] = 1

		if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
			return 0

		def recursive(i,j):
			if i>m-1 or j>n-1:
				return 0
			if dp[i][j]:
				return dp[i][j]
			if obstacleGrid[i][j] == 1:
				return 0
			dp[i][j] = recursive(i, j+1) + recursive(i+1,j)

			print(dp)
			return dp[i][j]
		
		return recursive(0,0)

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]], Output = 2),
			 dict(obstacleGrid = [[0,1],[0,0]], Output = 1),
			 dict(obstacleGrid = [[0,1,0],[0,0,0],[1,0,0]], Output = 2),
			 dict(obstacleGrid = [[0,0,0,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], Output = 9),
			 dict(obstacleGrid = [[0,0,1],[0,0,0],[1,0,0]], Output = 4),
			 dict(obstacleGrid = [[0,0,0,1],[0,1,0,0],[1,0,1,0]], Output = 1),
			 dict(obstacleGrid = [[0,1,0,0],[0,0,0,1],[0,0,0,0]], Output = 3)]
	for test in tests:
		assert sol.uniquePathsWithObstacles(test['obstacleGrid']) == test['Output']
		print('-------------------------------------')