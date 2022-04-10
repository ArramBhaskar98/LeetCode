class Solution:
	def maximumGap(self, nums):
		nums.sort()
		maxgap = 0
		for i in range(len(nums)-1):
			maxgap = max(maxgap, nums[i+1] - nums[i])
		return maxgap
		
if __name__ == '__main__':
	sol = Solution()
	tests = [dict(nums = [3,6,9,1], Output = 3),
			dict(nums = [10], Output = 0)]
	for test in tests:
		assert sol.maximumGap(test['nums']) == test['Output']
		print('--------------------------')