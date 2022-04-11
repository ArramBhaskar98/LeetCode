class Solution:
	def minDistance(self, word1, word2):
		m = len(word1)
		n = len(word2)

		# m+1 and n+1 is for padding whitespace to represent empty string
		longest_common_seq = [[ 0 for _ in range(m+1) ] for _ in range(n+1) ]

		# update dp table
		for i in range(n):
			for j in range(m):
				if word1[j] == word2[i]:
					# current character is the same, growing on previous substring
					longest_common_seq[i+1][j+1] = longest_common_seq[i][j] + 1
				else:
					# current characters are different, backtracking to subcases
					longest_common_seq[i+1][j+1] = max(longest_common_seq[i+1][j], longest_common_seq[i][j+1])
				print(longest_common_seq)
			print('**********')
		# get length of common characters
		length_of_common = longest_common_seq[n][m]

		# compute length of difference, which is the total counts of deletion
		length_of_difference = (m - length_of_common) + (n - length_of_common)

		# print('Longes seq: ', longest_common_seq)
		print('Length of common: ', length_of_common)
		print('length_of_difference: ', length_of_difference)

		return length_of_difference

if __name__ == '__main__':
	sol = Solution()
	tests = [
			dict(word1 = "sea", word2 = "eat", Output = 2),
			dict(word1 = "leetcode", word2 = "etco", Output = 4)]
	for test in tests:
		assert sol.minDistance(test['word1'], test['word2']) == test['Output']
		print('----------------------------------------')