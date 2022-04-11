# Given Hints in the problem understand it clearly so that you'll get solution

import heapq
class Solution:
	def isPossible(self, target):
		total = sum(target)
		A = [-x for x in target]
		print('Original Array: ',A)
		heapq.heapify(A)
		while True:
			a = -heapq.heappop(A)
			total -= a
			if a == 1 or total == 1:
				return True
			if a < total or total == 0 or a % total == 0:
				return False
			a %=  total
			total += a

			heapq.heappush(A, -a)
			print('Modified Array: ',A)


if __name__ == '__main__':
	sol = Solution()
	tests = [dict(target = [9,3,5], Output = True),
			dict(target = [1,1,1,2], Output = False),
			dict(target = [8,5], Output = True)]
	for test in tests:
		assert sol.isPossible(test['target']) == test['Output']
		print('---------------------------------------')