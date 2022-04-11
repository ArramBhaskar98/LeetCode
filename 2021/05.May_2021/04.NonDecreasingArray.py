class Solution:
	def checkPossibility(self, nums):
		count = 0
		for i in range(len(nums)-1):
			if nums[i+1]-nums[i]<0:
				count += 1
			if (i>1 and nums[i]-nums[i-2]<0 and nums[i+1]-nums[i-1]<0) or count > 1:
				return False
		return True

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(nums = [4,2,3], Output = True),
			dict(nums = [4,2,1], Output = False),
			dict(nums = [1,2,3,4,3,5,6,7,8], Output = True),
			dict(nums = [3,4,2,3], Output = False),
			dict(nums = [5,7,1,8], Output = True),
			dict(nums = [-1,4,2,3], Output = True)]
	for test in tests:
		assert sol.checkPossibility(test['nums']) == test['Output']
		print('---------------------------')