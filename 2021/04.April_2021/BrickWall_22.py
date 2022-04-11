
class Solution:
	def leastBricks(self, wall):
		d = {}
		maxSum = 0
		for row in wall:
			currSum = 0
			for bricks in row[:-1]:
				currSum += bricks
				if currSum not in d:
					d[currSum] = 0
				d[currSum] += 1
				print(d)
				maxSum = max(maxSum, d[currSum])
		return len(wall)-maxSum

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(wall = [[1,2,2,1],[3,1,2],[1,3,2],[2,4],[3,1,2],[1,3,1,1]], output = 2),
			 dict(wall = [[1],[1],[3]], output = 3)]
	
	for test in tests:
		assert sol.leastBricks(test['wall']) == test['output']
		# result = sol.leastBricks(test['wall'])
		# print(result)
		print('-------------------------------------')

