class Solution:
	def maxProduct(self, words):
		max_value = 0
		words.sort(key = lambda x: len(x), reverse = True)
		x = len(words)
		i =0
		while i < x:
			j = i + 1
			while j < x:
				flag = 0
				for k in set(words[i]):
					if k in set(words[j]):
						flag = 1
						break
				if flag == 0:
					print(words[i], words[j])
					res = len(words[i]) * len(words[j])
					max_value = max(res, max_value)
					x = j
					break
				j += 1
			i += 1
			
		return max_value

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(words = ["abcw","baz","foo","bar","xtfn","abcdef"], Output = 16),
			dict(words = ["a","ab","abc","d","cd","bcd","abcd"], Output = 4),
			dict(words = ["a","aa","aaa","aaaa"], Output = 0)]
	for test in tests:
		assert sol.maxProduct(test['words']) == test['Output']
		print('------------------------------------------')