class Solution:
	def findAndReplacePattern(self, words, pattern):
		# Final List
		lst = []
		# Checking for each word in words list
		for word in words:
			# for each word dictionary is created
			d = {}
			flag = 0
			# This is looped based on length of current word in words list
			for i in range(len(word)):
				# if current letter in pattern not in dictionary, go further
				if pattern[i] not in d:
					# if current word is already in dictionary values, so don't map 
					# current-pattern-letter to already placed current-word-letter
					# bijective- no two pattern-letters map the same word-letter
					if word[i] in d.values():
						flag = 1
						break
					# If there is no pattern-letter mapped current-word-letter, so insert this
					# pattern-letter into dictionary
					d[pattern[i]]=word[i]
				else:
					if d[pattern[i]]!=word[i]:
						flag=1
						break
			if flag==0:
				lst.append(word)

		print(lst)
		return lst

if __name__ == '__main__':
	sol = Solution()
	tests = [
			dict(words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb", 
				Output = ["mee","aqq"]),
			dict(words = ["a","b","c"], pattern = "a", Output = ["a","b","c"]),
			dict(words = ["abcd", "abba", "bqqr", "bbba", "abbb"], pattern = "pqqs", Output = ["bqqr"])]
	for test in tests:
		assert sol.findAndReplacePattern(test['words'], test['pattern']) == test['Output']
		print('---------------------------------------------------------')