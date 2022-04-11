class Solution:
	def minimumTotal(self, triangle):
		memo = {}
		def dfs(t, r, c):
			if r == len(t):
				return 0
			if (r,c) in memo:
				return memo[(r,c)]
			memo[(r,c)] = t[r][c] + min(dfs(t, r+1, c), dfs(t, r+1,c+1))
			print(memo)
			return memo[(r,c)]

		return dfs(triangle, 0, 0)

		# for r in range(1,len(triangle)):
		# 	triangle[r][0] += triangle[r-1][0]
		# 	triangle[r][-1]+= triangle[r-1][-1]
		# 	for c in range(1,r):
		# 		triangle[r][c] += min(triangle[r-1][c-1], triangle[r-1][c])
		# return min(triangle[-1])
		# tsum = 0
		# for item in triangle:
		# 	tsum = tsum + min(item)
		# return tsum

if __name__ == '__main__':
	sol = Solution()

	tests = [dict(triangle = [[2],[3,4],[6,5,7],[4,1,8,3]], output = 11),
			 dict(triangle = [[-10]], output = -10),
			 dict(triangle = [[-1],[2,3],[1,-1,-3]], output = -1)]

	for test in tests:
		assert sol.minimumTotal(test['triangle']) == test['output']
		print('-----------------------')
