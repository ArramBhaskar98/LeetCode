class Solution:
    @staticmethod
    def longestPalindrome(s):
        # Method -2 -> Linear Solution - O(n)
        n = len(s)
        if len(set(s)) == 1:
            return s
        if n == 2:
            if s == s[::-1]:
                return s
            else:
                return s[0]
        start = 0
        maxlen = 1
        for i in range(n):
            if i - maxlen >= 1 and s[i - maxlen - 1 : i + 1] == s[i - maxlen - 1 : i + 1][::-1]:
                start = i-maxlen-1
                maxlen += 2
                continue
            if i - maxlen >= 0 and s[i - maxlen : i + 1] == s[i - maxlen : i + 1][::-1]:
                start = i-maxlen
                maxlen += 1
        return s[start : start + maxlen]

        # Method - 1 -> BruteForce solution - O(n**2)
        n = len(s)
        if len(set(s)) == 1:
            return s
        if n == 2:
            if s == s[::-1]:
                return s
            else:
                return s[0]
        ans = ""
        for i in range(n):
            for j in range(i+1, n):
                temp = s[i:j+1]
                if temp == temp[::-1] and len(temp) > len(ans):
                    ans = temp
        if not ans:
            return s[0]
        else:
            return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(s = "babad", Output = "bab"),
             dict(s = "cbbd", Output = "bb"),
             dict(s = "abcba", Output = "abcba"),
             dict(s = "abccba", Output = "abccba")]
    for test in tests:
        output = sol.longestPalindrome(test['s'])
        print(output)
        assert output == test['Output']
        print("-----------------------------------------------")