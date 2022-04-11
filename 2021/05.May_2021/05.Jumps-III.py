class Solution:
	def jump(self, nums):
		jump = 0
		max_jump = 0
		curr_index = 0
		for i in range(len(nums)-1):
			max_jump = max(max_jump, i+nums[i])
			if curr_index == i:
				jump += 1
				curr_index = max_jump
		return jump	

if __name__ == '__main__':
	sol = Solution()
	tests = [
			dict(nums = [2,3,1,1,4], Output = 2),
			dict(nums = [2,3,0,1,4], Output = 2),
			dict(nums = [3,2,4,5,1,1,6,2,1,3], Output = 3),
			dict(nums = [0], Output = 0),
			dict(nums = [2,2,3],Output = 1),
			dict(nums = [3,2,1], Output = 1),
			dict(nums = [1,2], Output = 1),
			dict(nums = [2,1], Output = 1),
			dict(nums = [2,3,1], Output = 1),
			dict(nums = [1,1,2,1,1], Output = 3),
			dict(nums = [8,6,5,4,3,2,1,1,1], Output = 1)]
	for test in tests:
		assert sol.jump(test['nums']) == test['Output']
		print('--------------------------') 
