class Solution:
	def countBinarySubstrings(self, s):
		prevBlock = 0
		currBlock = 1
		binSums = 0
		currChar = s[0]
		for item in range(1, len(s)):
			if s[item] == currChar:
				currBlock += 1
			else:
				binSums += min(prevBlock, currBlock)
				prevBlock = currBlock
				currBlock = 1
			currChar = s[item]
		binSums += min(prevBlock, currBlock)
		return binSums

		# The below program is working for smaller inputs but not for larger string say len(s) > 5000
		# count = 0
		# for i in range(len(s)):
		# 	for j in range(i+2, len(s)+1,2):
		# 		sliced = s[i:j]
		# 		target = len(sliced)//2
		# 		if '0'*target + '1'*target == sliced or '1'*target + '0'*target == sliced:
		# 			count += 1
		# 			print(sliced)
		# return count

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(s = '00110011', output = 6),
			 dict(s = '10101', output = 4),
			 dict(s = '000111', output = 3),
			 dict(s = '11100', output = 2),
			 dict(s = '00011100', output = 5),
			 dict(s = '00110', output = 3)
			 ]
	for test in tests:
		assert sol.countBinarySubstrings(test['s']) == test['output']
		print('-------------------------')