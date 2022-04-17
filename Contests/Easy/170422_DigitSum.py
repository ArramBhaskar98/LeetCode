class Solution:
    def digitSum(self, s: str, k: int):
        if len(s) <= k:
            return s
        ans = ""
        while len(s) > k:
            temp1 = ""
            for i in range(0, len(s), k):
                temp2 = 0
                for j in s[i:i + k]:
                    temp2 += int(j)
                temp1 += str(temp2)
            s = temp1
            ans = s
        return ans

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(s = "11111222223", k = 3, Output = "135"),
             dict(s = "00000000", k = 3, Output = "000"),
             dict(s = "123", k = 3, Output = "123"),
             dict(s = "1", k = 2, Output = "1")]
    for test in tests:
        assert sol.digitSum(test['s'], test['k']) == test['Output']
        print("--------------------------------------------")