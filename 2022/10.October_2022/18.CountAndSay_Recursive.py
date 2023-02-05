# Problem : https://leetcode.com/problems/count-and-say/


class Solution:
    def countAndSay(self, n: int) -> str:

        def recursive(k):
            if k == 1:
                return "1"
            string = recursive(k - 1) + '#'
            count = 1
            new_s = ''
            for i in range(len(string) - 1):
                if string[i] == string[i + 1]:
                    count += 1
                else:
                    new_s += str(count) + string[i]
                    count = 1
            return new_s

        return recursive(n)


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(n = 1, Output = "1"),
             dict(n = 4, Output = "1211")]
    for test in tests:
        assert sol.countAndSay(test['n']) == test['Output'],"Test Case Failed....!"
        print("-------------------------------------")