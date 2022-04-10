class Solution:
	def toLowerCase(self, s):
		return s.lower()
if __name__ == '__main__':
	sol = Solution()
	tests = [dict(s = "Leetcode", Output = 'leetcode'),
			dict(s = "Arram", Output = 'arram')]
	for test in tests:
		assert sol.toLowerCase(test['s']) == test['Output']
		print('----------------------')