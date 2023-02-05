from collections import Counter
from typing import List
# Problem : https://leetcode.com/problems/set-mismatch/


class Solution:
    def findErrorNums(self, nums: List[int]) -> List[int]:
        d = Counter(nums)
        duplicate_number = d.most_common(1)[0][0]
        for i in range(1, len(nums)+1):
            if i not in d:
                return [duplicate_number, i]

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,2,2,4], Output = [2,3]),
             dict(nums = [1,1], Output = [1,2]),
             dict(nums = [2,2], Output = [2,1])]
    for test in tests:
        assert sol.findErrorNums(test['nums']) == test['Output'], "Test Case Failed...!"
        print("----------------------------------------------")