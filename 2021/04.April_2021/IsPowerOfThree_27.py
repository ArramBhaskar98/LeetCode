class Solution:
	def isPowerOfThree(self, n):
		i = 1
		if n<1:
			return False
		while i<=n:
			if i == n:
				return True
			else:
				i = 3 * i
		return False
		# The below code is satisfied if -31<n<31
		# i = 1
		# if n>1:
		# 	while i<=n:
		# 		if i == n:
		# 			return True
		# 		else:
		# 			i = 3 * i
		# 	return False
		# else:
		# 	i = -1
		# 	while i>=n:
		# 		if i == n:
		# 			return True
		# 		else:
		# 			i = 3 * i
		# 	return False


if __name__ == '__main__':
	sol = Solution()
	tests = [dict(n = 27, result = True),
	 		 dict(n = 0, result = False),
	 		 dict(n = 9, result = True),
	 		 dict(n = 45, result = False),
	 		 dict(n = 81, result = True),
	 		 dict(n = 60, result = False),
	 		 dict(n = 1073741824, result = False)]
	for test in tests:
		assert sol.isPowerOfThree(test['n']) == test['result']
		print('---------------------')
