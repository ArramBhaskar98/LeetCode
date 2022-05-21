# Refer to the Problem Question here : https://leetcode.com/problems/decode-ways/

class Solution:
    def numDecodings(self, s: str) -> int:

        # Top-Down Approach
        n = len(s)
        dp = [0]*(n+1)
        dp[0] = 1
        for i in range(1, n+1):
            if s[i-1] != "0":
                dp[i] = dp[i-1]
            else:
                dp[i] = 0
            if i > 1 and s[i-2] != "0" and 1 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        return dp[-1]

        # Bottom-up approach
        dp = {}
        def recursive(st):
            if len(st) == 0:
                return 1
            if st in dp:
                return dp[st]

            # Initially for every possible string we go with 0 number of ways
            x = 0
            if st[0] != "0":          # If first element is zero, simply returning 0 combination starting with 0
                x += recursive(st[1:])      # Now checking the same string from 1st index
                if 1 <= int(st[:2]) <= 26 and len(st) > 1:  # If string of 2 digits lies between 1 to 26, then check that same string from 2nd index to last index of string
                    x += recursive(st[2:])
            dp[st] = x
            return x
        return recursive(s)


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(s = "12", Output = 2),
             dict(s = "226", Output = 3),
             dict(s = "06", Output = 0),
             dict(s = "074847", Output = 0)]
    for test in tests:
        assert sol.numDecodings(test['s']) == test['Output']
        print("--------------------------------------------")