# Algorithm
# 1. declare a dictionary of key with it's associated value
# 2. Take one empty list and check if given input key is present in dictionary, then append 
# it's as associated value to that list
# 3. Next send that list iterables to itertools.product()
# 4. finally join the each tuple elements with no ','(comma) separated values.

from itertools import product
def combinationsPhoneNumber(digits):
	if not digits:
		return []
	
	d = {'2' : 'abc',
		 '3' : 'def',
		 '4' : 'ghi',
		 '5' : 'jkl',
		 '6' : 'mno',
		 '7' : 'pqrs',
		 '8' : 'tuv',
		 '9' : 'wxyz'}

	lst = []
	for item in digits:
		if item in d:
			lst.append(d.get(item))
	result = list(product(*lst))

	final_res = [''.join(x) for x in result]

	return final_res

if __name__ == '__main__':

	# TestCases
	tests = [dict(digits = "23", result = ["ad","ae","af","bd","be","bf","cd","ce","cf"]),
			 dict(digits = "", result = []),
			 dict(digits = "2", result = ["a","b","c"])]
	for test in tests:
		assert combinationsPhoneNumber(test['digits']) == test['result']
		print("-------------------------")