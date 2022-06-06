from collections import Counter

class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        """ The Main aim of the problem is to check how many copies of target can be formulated from s """
        d1 = Counter(s)
        d2 = Counter(target)
        ans = float('inf')
        for letter, count in d2.items():
            if letter in d1:
                ans = min(ans, d1[letter]//count)
            else:
                return 0
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(s = "ilovecodingonleetcode", target = "code", Output = 2),
             dict(s = "abcba", target = "abc", Output = 1),
             dict(s = "abbaccaddaeea", target = "aaaaa", Output = 1),
             dict(s = "abc", target = "def", Output = 0)]
    for test in tests:
        assert sol.rearrangeCharacters(test['s'], test['target']) == test['Output']
        print("---------------------------------------------------------")