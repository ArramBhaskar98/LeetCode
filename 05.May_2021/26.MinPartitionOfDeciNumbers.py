class Solution:
	def minPartitions(self, n):
		# This list is used to see how many combinations is possible
		lst = []
		for i in range(int(max(n)), 0, -1):
			s = ''
			for j in n:
				if int(j) >= i:
					s += '1'
				else:
					s += '0'
			lst.append(s)
		print(lst)

		# This is direct method without any logic
		return int(max(n))
		
if __name__ == '__main__':
	sol = Solution()
	tests = [dict(n = "32", Output =3),
			dict(n = "82734", Output = 8),
			dict(n = "27346209830709182346", Output = 9)]
	for test in tests:
		assert sol.minPartitions(test['n']) == test['Output']
		print('----------------------------------')