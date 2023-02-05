class Solution:
    def numDecodings(self, s: str) -> int:
        # Optimized Version (Run-Time)
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        dp[1] = 1 if s[0] != '0' else 0
        for i in range(2, n+1):
            curr = int(s[i-1])
            prev = int(s[i-2])
            if curr != 0:
                dp[i] += dp[i-1]
            if prev != 0 and (10*prev) + curr <= 26:
                dp[i] += dp[i-2]
        return dp[n]

        # My Approach
        dp = {}

        def recursive(st):
            if st in dp:
                return dp[st]
            if len(st) == 0:
                return 1
            x = 0
            if st[0] != '0':
                x += recursive(st[1:])
                if 1 <= int(s[:2]) <= 26 and len(st) > 1:
                    x += recursive(st[2:])
            dp[st] = x
            return x
        return recursive(s)


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(s = "12", Output = 2),
             dict(s = "226", Output = 3),
             dict(s = "06", Output = 0),
             dict(s = "10025", Output = 0),
             dict(s = "99999", Output = 1)]
    for test in tests:
        assert sol.numDecodings(test['s']) == test['Output']
        print("Test Case Passed")