class Solution:
    def shortestPath(self, grid, k):

    	def recursive():
    		if :
    		return -1


    	return k

if __name__ == '__main__':

	sol = Solution()
	tests = [dict(grid = [[0,0,0], [1,1,0], [0,0,0], [0,1,1], [0,0,0]], k = 1, Output = 6),
			dict(grid = [[0,1,1], [1,1,1], [1,0,0]], k = 1, Output = -1)]
	for test in tests:
		assert sol.shortestPath(test['grid'], test['k']) == test['Output']
		print("--------------------------------------------------------")