class Solution:
    def removeAnagrams(self, words):
        i = 1
        while i < len(words):
            if sorted(words[i]) == sorted(words[i-1]):
                words.remove(words[i])
                continue
            i += 1
        return words


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(words = ["abba","baba","bbaa","cd","cd"], Output = ["abba","cd"]),
             dict(words = ["a","b","c","d","e"], Output = ["a","b","c","d","e"]),
             dict(words = ["z","z","z","gsw","wsg","gsw","krptu"], Output = ["z","gsw","krptu"])]
    for test in tests:
        assert sol.removeAnagrams(test['words']) == test['Output']
        print("-------------------------------------------------")