class Solution:
	def minMoves2(self, nums):
		count = 0
		nums.sort()
		middle_element = nums[len(nums)//2]
		for item in nums:
			count += abs(middle_element-item)
		return count

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(nums = [1,2,3], Output = 2),
			dict(nums = [1,10,2,9], Output = 16),
			dict(nums = [1, 2, 3, 58, 34, 89, 92, 5, 5, 5, 5, 66, 101], Output = 419),
			dict(nums = [1], Output = 0),
			dict(nums = [1,2], Output = 1)]
	for test in tests:
		assert sol.minMoves2(test['nums']) == test['Output']
		print('---------------------------------------')