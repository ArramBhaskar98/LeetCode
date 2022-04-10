class Solution:
	def maxScore(self, cardPoints, k):
		n = len(cardPoints)
		total_pts = sum(cardPoints)
		
		windowSize = n-k
		sumOfWindow = sum(cardPoints[:windowSize])
		max_pts = 0

		for i in range(k+1):
			if i > 0:
				sumOfWindow -= cardPoints[i-1]
				sumOfWindow += cardPoints[i+windowSize-1]
			max_pts = max(max_pts, total_pts-sumOfWindow)
		return max_pts

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(cardPoints = [1,2,3,4,5,6,1], k = 3, Output = 12),
			dict(cardPoints = [2,2,2], k = 2, Output = 4),
			dict(cardPoints = [9,7,7,9,7,7,9], k = 7, Output = 55),
			dict(cardPoints = [1,1000,1], k = 1, Output = 1),
			dict(cardPoints = [1,79,80,1,1,1,200,1], k = 3, Output = 202)]
	for test in tests:
		assert sol.maxScore(test['cardPoints'], test['k']) == test['Output']
		print('----------------------------------------------------')