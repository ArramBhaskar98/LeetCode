# Method-1 is the Naive method and it is not optimal when left and right given high range.
# Method-2 is the Optimal which generates palindrome and check it's square also a palindrome. This
# is suitable even left and right given as high range.
import math
class Solution:
	def superpalindromesInRange(self, left, right):
		
		# Method - 1
		def reverse(x):
			num = 0
			while x:
				num = num * 10 + x%10
				x //= 10
			return num
		m = int(left)
		n = int(right)
		i = math.floor(math.sqrt(m))
		print(i)
		j = 1
		cnt = 0
		while i <= n and j <= n:
			res = i*i
			if res >= m and res <=n and res // 10 == 0:
				cnt += 1
			elif i%11 != 0:
				i += 1
				continue
			elif res >= m and res <= n:
				inc_num = i
				sqr_num = res
				sqr_dig = 0
				inc_dig = reverse(inc_num)

				if inc_dig == i:
					sqr_dig = reverse(sqr_num)

				if sqr_dig == res and inc_dig == i:
					print(i, inc_dig,"---------", res, sqr_dig)
					cnt += 1
			i += 1
			j = res
		print('Count Till Now: ',cnt)
		return cnt

		# Method-2 Optimal Solution

		# L = int(left)
		# R = int(right)
		# MAGIC = 100000

		# def reverse(x):
		# 	sqr_dig = 0
		# 	while x:
		# 		sqr_dig = sqr_dig * 10 + x%10
		# 		x //= 10
		# 	return sqr_dig

		# def palindrome(x):
		# 	return x == reverse(x)

		# cnt = 0

		# # For Odd Length
		# for i in range(MAGIC):
		# 	s = str(i)		    # 123
		# 	t = s + s[-2::-1]   # 12321
		# 	sq = int(t) ** 2
		# 	if sq > R:
		# 		break
		# 	if sq >= L and palindrome(sq):
		# 		cnt += 1

		# # For even length
		# for j in range(MAGIC):
		# 	s = str(j)			# 1234
		# 	t = s + s[::-1]		# 12344321
		# 	sq = int(t) ** 2
		# 	if sq > R:
		# 		break
		# 	if sq >= L and palindrome(sq):
		# 		cnt += 1
		# print(cnt)
		# return cnt

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(left = "4", right = "1000", Output = 4),
			dict(left = "1", right = "2", Output = 1),
			dict(left = "6", right = "1000", Output = 3),]
			# dict(left = "40000000000000000", right = "50000000000000000", Output = 2)]
	for test in tests:
		assert sol.superpalindromesInRange(test['left'], test['right']) == test['Output']
		print('--------------------------------------')