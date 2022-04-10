class Solution:
    def fib(self, n: int) -> int:
        if n==0:
            return 0
        elif n==1:
            return 1
        else:
            self.result = self.fib(n-1) + self.fib(n-2)
        return self.result

solution = Solution()
result = solution.fib(4)
print('Final Result: ', result)