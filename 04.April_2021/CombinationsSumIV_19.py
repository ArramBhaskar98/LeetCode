from itertools import product
class Solution:
	def combinationSum4(self, nums, target):
		combs = [0] * (target + 1)
		combs[0] = 1
		for t in range(1, target + 1):
			for n in nums:
				if t >= n:
					combs[t] += combs[t-n]
					print(combs)
		return combs[target]
    	# nums = [str(x) for x in nums]
    	# result_lst = []

    	# st = ''
    	# for x in nums:
    	# 	st = st + x

    	# i = 0
    	# while i<target:
    	# 	n = target-i
    	# 	res = list(product(st, repeat = n))

    	# 	for item in res:
    	# 		lst = list(item)
    	# 		int_lst = [int(x) for x in lst]
    	# 		if sum(int_lst) == target:
    	# 			result_lst.append(lst)
    	# 		else:
    	# 			continue
    	# 	i = i+1
    	# return len(result_lst)   



if __name__ == '__main__':
	sol = Solution()
	tests = [dict(nums = [1,2,3], target = 4, result = 7),
			 dict(nums = [9], target = 3, result = 0),
			 dict(nums = [3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25], target = 1, result=0)]

	for test in tests:
		assert sol.combinationSum4(test['nums'], test['target']) == test['result']
		print('------------------------------------')