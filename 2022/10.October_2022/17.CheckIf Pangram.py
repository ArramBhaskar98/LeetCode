from collections import Counter

# Solution Tips
# * For this kind of problems one must need to think what data structure help us to store the unique values

class Solution:
    def checkIfPangram(self, sentence: str) -> bool:
        # Method-2
        s = set()
        for char in sentence:
            s.add(char)
        return len(s) == 26

        # method-1
        d = Counter(sentence)
        for i in range(97, 123):
            if chr(i) not in d:
                return False
        return True


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(sentence = "thequickbrownfoxjumpsoverthelazydog", Output = True),
             dict(sentence = "leetcode", Output = False)]
    for test in tests:
        assert sol.checkIfPangram(test['sentence']) == test['Output'], "Test Case Failed...!"
        print("---------------------------------")