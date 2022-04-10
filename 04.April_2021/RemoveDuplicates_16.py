
class Solution:
	def removeDuplicates(self, s, k):
		for i in range(len(s) - k, -1, -1):
			if s[i] * k == s[i : i + k]:
				s = s[:i] + s[i + k :]
		return s
		# for i in range(k-1,len(s)):
		# 	if s[i] * k == s[i-k+1: i+1]:
		# 		s = s[:i-k+1] + s[i:]
		# return s
		# d = {}
		# if len(s) == len(set(s)):
		# 	return s
		# else:
		# 	for item in s:
		# 		if item not in d:
		# 			d[item] = 1
		# 		else:
		# 			d[item] += 1
		# 			if d[item] == k:
		# 				del d[item]
		# 			else:
		# 				print('dict: ',d)
		# 				continue

		# 	s2 = ''

		# 	for item,value in d.items():
		# 		s2 = s2+ item*value

		# 	print('s2: ',s2)
			# return s2

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(s = 'abcd', k = 2, result = 'abcd'),
			 dict(s = 'deeedbbcccbdaa', k = 3, result = 'aa'),
			 dict(s = 'pbbcggttciiippooaais', k = 2, result = 'ps'),
			 dict(s = "yfttttfbbbbnnnnffbgffffgbbbbgssssgthyyyy", k = 4, result = 'ybth')]
	for test in tests:
		assert sol.removeDuplicates(test['s'], test['k']) == test['result']
		print('--------------------------------------')