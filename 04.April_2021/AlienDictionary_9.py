# Algorithm
# 1. From words list, each word is getting the index's of each character that is present in order string.
# 2. After completion of all words sorting based on the 1st step

def isAlienSorted(words, order):
	print('Sorted words: ', sorted(words))
	print(sorted(words, key=lambda word: [order.index(char) for char in word]))
	for word in words:
		print([order.index(char) for char in word])

	return words == sorted(words, key=lambda word: [order.index(char) for char in word])

if __name__ == '__main__':
	
	# TestCases
	tests = [dict(words = ["hello","leetcode"], order = "hlabcdefgijkmnopqrstuvwxyz",
			 	result = True),
			 dict(words = ["word","world","row"], order = "worldabcefghijkmnpqstuvxyz",
			 	result = False),
			 dict(words = ["apple","app"], order = "abcdefghijklmnopqrstuvwxyz",
			 	result = False)]

	for test in tests:
		assert isAlienSorted(test['words'], test['order']) == test['result']
		# result = isAlienSorted(test['words'], test['order'])
		# print('Final Result: ', result)
		print('--------------')