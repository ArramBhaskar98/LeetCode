class Solution:
    def removeDigit(self, number, digit):
        """ The main aim of this problem is to remove the given digit from number and get the maximum number """
        end = len(number) - 1
        ans = 0
        for i in range(end, -1, -1):
            if number[i] == digit and i == end:
                ans = max(ans, int(number[:i]))
            elif number[i] == digit:
                ans = max(ans, int(number[:i] + number[i + 1:]))
        return str(ans)


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(number="123", digit="3", Output="12"),
             dict(number="1231", digit="1", Output="231"),
             dict(number="551", digit="5", Output="51"),
             dict(number="12321", digit="2", Output="1321")]
    for test in tests:
        assert sol.removeDigit(test['number'], test['digit']) == test['Output']
        print("---------------------------------------------")
