from itertools import accumulate
class Solution:
	def runningSum(self, nums):
		# Method-1
		for i in range(1, len(nums)):
			nums[i] = nums[i-1] + nums[i]
		return nums

		# Method-2
		# res = list(accumulate(nums))
		# return res
		
if __name__ == '__main__':
	sol = Solution()
	tests = [dict(nums = [1,2,3,4], Output = [1,3,6,10]),
			dict(nums = [1,1,1,1,1], Output = [1,2,3,4,5]),
			dict(nums = [3,1,2,10,1], Output = [3,4,6,16,17])]
	for test in tests:
		assert sol.runningSum(test['nums']) == test['Output']
		print('-------------------------')