from collections import defaultdict
from typing import List

""" Default Dictionary will help us group the similar anagrams into single list """

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        for word in strs:
            a = "".join(sorted(word))
            d[a].append(word)
        return list(d.values())


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(strs = ["eat","tea","tan","ate","nat","bat"], Output = [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]),
             dict(strs = [""], Output = [[""]]),
             dict(strs = ["a"], Output = [["a"]])]
    for test in tests:
        assert sol.groupAnagrams(test['strs']) == test['Output']
        print("------------------------------------------------")