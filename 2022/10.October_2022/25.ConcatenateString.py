from typing import List
# Problem - https://leetcode.com/problems/check-if-two-string-arrays-are-equivalent/

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        # Method -1
        return "".join(word1) == "".join(word2)

        # Method-2
        s1, s2 = '', ''
        for word in word1:
            s1 += word
        for word in word2:
            s2 += word
        return s1 == s2


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(word1 = ["ab", "c"], word2 = ["a", "bc"], Output = True),
             dict(word1 = ["a", "cb"], word2 = ["ab", "c"], Output = False),
             dict(word1  = ["abc", "d", "defg"], word2 = ["abcddefg"], Output = True)]
    for test in tests:
        assert sol.arrayStringsAreEqual(test['word1'], test['word2']) == test['Output']
        print("----------------------------------------------------------")