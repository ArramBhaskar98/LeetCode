from collections import Counter
from typing import List
# Problem - https://leetcode.com/problems/top-k-frequent-words/


class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        """ This problem can be solved in two ways
        1.  First sort the words (this return the words in ascending order )
            Apply Counter collection method, this will return the key, value pairs in ascending order
            then Applying most_common(k) will return the most frequency elements
        2.  First Applying the Counter method on words and sorting by the frequency from highest to lowest.
            Sort the words with the same frequency by their lexicographical order."""

        # Method-2
        words.sort()
        d1 = [x[0] for x in Counter(words).most_common(k)]
        print(d1)
        return d1

        # Method - 1
        d = Counter(words)
        return sorted(d, key = lambda x: (-d[x],x))[:k]

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(words = ["i","love","leetcode","i","love","coding"], k = 2, Output = ["i","love"]),
             dict(words = ["the","day","is","sunny","the","the","the","sunny","is","is"], k = 4, Output = ["the","is","sunny","day"]),
             dict(words = ["i","love","leetcode","i","love","coding"], k = 3, Output = ["i","love","coding"]),
             dict(words = ["i","love","leetcode","i","love","coding","leetcode"], k = 4, Output = ["i","leetcode","love","coding"])]
    for test in tests:
        assert sol.topKFrequent(test['words'], test['k']) == test['Output'], "Test Case Failed....!"
        print("------------------------------------------")