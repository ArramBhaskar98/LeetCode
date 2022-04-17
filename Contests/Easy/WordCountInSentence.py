import re
class Solution:
    def countValidWords(self, sentence: str) -> int:
        return len(list(filter(lambda x: re.match(r'^[a-z]*([a-z]-[a-z])?[a-z]*[!\.,]?$',x),sentence.split())))
if __name__ == "__main__":
    sol = Solution()
    tests = [dict(sentence = "cat and  dog", Output = 3),
            dict(sentence = "!this  1-s b8d!", Output = 0),
            dict(sentence = "alice and  bob are playing stone-game10", Output = 5),
            dict(sentence = "he bought 2 pencils, 3 erasers, and 1  pencil-sharpener.", Output = 6),
            dict(sentence = "he bought 2 pencils cat-", Output = 3)]
    for test in tests:
        assert sol.countValidWords(test['sentence']) == test['Output']
        print('-----------------------------------------------------')