# by method of Sieve of Eratosthenes
import math
class Solution:

	# Method-1
	def countPrimes(self, n):
		if n <= 2:
			return 0
		
		primes = {}
		for i in range(2, int(math.sqrt(n))+1):
			if i not in primes:
				for multiple in range(i*i, n, i):
					primes[multiple] = 1
		cnt = n-len(primes)-2
		print('Count = ',cnt)
		return cnt

	# Method - 2
	def countPrimes(self, n):
		isPrime = [True]*n
		for i in range(2, int(math.sqrt(n))+1):
			if isPrime[i] != True:
				continue
			for j in range(i*i, n, i):
				isPrime[j] = False
		count = 0
		for i in range(2, n):
			if isPrime[i]:
				count += 1
		print('Count = ', count)
		return count

	# Method-3
	def countPrimes(self, n):
		if n<3:
			return 0
		isPrime = [True]*n
		isPrime[0] = isPrime[1] = False
		for i in range(2, int(math.sqrt(n))+1):
			isPrime[i*i:n:i] = [False]*((n-1-i*i)//i+1)
		return sum(isPrime)


if __name__ == '__main__':
	sol = Solution()
	tests = [dict(n = 10, Output = 4),
			dict(n = 0, Output = 0),
			dict(n = 1, Output = 0),
			dict(n = 100, Output = 25),
			dict(n = 1000, Output = 168),
			dict(n = 100000, Output = 9592)]
	for test in tests:
		assert sol.countPrimes(test['n']) == test['Output']
		print('------------------------------------------')