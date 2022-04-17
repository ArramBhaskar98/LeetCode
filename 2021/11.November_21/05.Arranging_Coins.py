class Solution:
    def arrangeCoins(self, n: int) -> int:

        # Math Formulae
        return int((2*n + 0.25)**0.5 - 0.5)

        # Binary Search
        left, right = 0, n
        while left <= right:
            k = (left + right)//2
            curr = (k*(k+1))//2
            if curr == n:
                return k
            elif curr > n:
                right = k-1
            else:
                left = k+1
        return right

        # Normal Method -- O(k)
        if n <= 2:
            return 1
        if n <= 4:
            return 2
        for i in range(1, n-n//2+1):
            n -= i
            if n < 0:
                return i-1

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(n = 5, Output = 2),
            dict(n = 8, Output = 3),
            dict(n = 2, Output = 1)]
    for test in tests:
        assert sol.arrangeCoins(test['n']) == test['Output']
        print("-------------------------------------------")