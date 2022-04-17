class Solution:
    def hcf(self, a, b):
        if a == b:
            return a
        while b:
            temp = b
            b = a % b
            a = temp
        return a


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(a = 98, b = 56, Output = 14),
            dict(a = 14, b = 7, Output = 7),
            dict(a = 7, b = 14, Output = 7)]
    for test in tests:
        assert sol.hcf(test['a'], test['b']) == test['Output']
        print("----------------------------------------------")
