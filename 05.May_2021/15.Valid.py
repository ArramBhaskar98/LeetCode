import re
class Solution:
	def isNumber(self, s):
		return bool(re.match(r'^[+-]?(\d+\.\d+|\d+\.|\.\d+|\d+)([eE][+-]?\d+)?$',s))
		
if __name__ == '__main__':
	sol = Solution()
	tests = [
			dict(s = "+3.14", Output = True),
			dict(s = "3.143.14", Output = False),
			dict(s = "0", Output = True),
			dict(s = "e", Output = False),
			dict(s = ".", Output = False),
			dict(s = ".1", Output = True),
			dict(s = "abc", Output = False),
			dict(s = "1a", Output = False),
			dict(s = "1e", Output = False),
			dict(s = "e3", Output = False),
			dict(s = "99e2.5", Output = False),
			dict(s = "--6", Output = False),
			dict(s = "-+3", Output = False),
			dict(s = "95a54e53", Output = False),
			dict(s = "2e10", Output = True),
			dict(s = "0089", Output = True),
			dict(s = "-0.1", Output = True),
			dict(s = "+3e+7", Output = True),
			dict(s = "4.", Output = True),
			dict(s = "2e10", Output = True),
			dict(s = "-90E3", Output = True),
			dict(s = "+6e-7", Output = True),
			dict(s = "53.5e93", Output = True),
			dict(s = "-123.456e789", Output = True),
			dict(s = "2e10", Output = True)]
	i = 1
	for test in tests:
		assert sol.isNumber(test['s']) == test['Output']
		print(i,'-------------------------------------')
		i += 1