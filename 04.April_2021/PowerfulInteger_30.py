import itertools
class Solution:
	def powerfulIntegers(self, x, y, bound):
		lst = []
		xlst = []
		ylst = []
		i = 0
		if x == 1 or x == 0:
			xlst.append(x)
		else:
			while x**i <= bound:
				xlst.append(x**i)
				i += 1
		i = 0
		if y == 1 or y == 0: 
			ylst.append(y)
		else:
			while y**i <= bound:
				ylst.append(y**i)
				i += 1
		result = list(itertools.product(xlst, ylst))
		result = [item[0]+item[1] for item in result]
		result = list(set(result))

		for item in result:
			if item > bound:
				continue
			else:
				lst.append(item)
		return lst

		# Another approach without using itertools.product
		mySet = set()
		i, j = 0, 0
		while x**i <= bound:
			while x**i + y**j <= bound:
				mySet.add(x**i + y**j)
				j += 1
				if y == 1 or y == 0:
					break
			i += 1
			j = 0
			if x == 1 or x == 0:
				break
		print(list(mySet))
		return list(mySet)



if __name__ == '__main__':
	sol = Solution()
	tests = [dict(x = 2, y = 3, bound = 10, Output = [2,3,4,5,7,9,10]),
			 dict(x = 3, y = 5, bound = 15, Output = [2,4,6,8,10,14]),
			 dict(x = 2, y = 5, bound = 15, Output = [2,3,5,6,7,9,13]),
			 dict(x = 2, y = 1, bound = 10, Output = [9,2,3,5])]

	for test in tests:
		assert sol.powerfulIntegers(test['x'], test['y'], test['bound']) == test['Output']
		# result = sol.powerfulIntegers(test['x'], test['y'], test['bound'])
		# print(result)
		print('-------------------------------------------')
