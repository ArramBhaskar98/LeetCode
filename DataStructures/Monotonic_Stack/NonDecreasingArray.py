# Reference for Question : https://leetcode.com/problems/steps-to-make-array-non-decreasing/
# Monotonic Stack
from datetime import datetime as t


class Solution:
    def totalSteps(self, nums) -> int:
        """ The main aim of the problem is to make array in increasing order in number of steps """
        n = len(nums)
        dp = [0]*n
        stack = []
        ans = 0
        for i in range(n-1, -1, -1):
            while stack and nums[i] > nums[stack[-1]]:
                dp[i] = max(dp[i]+1, dp[stack.pop()])
            stack.append(i)
        print(dp)
        return dp[0]


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [5,3,4,4,7,3,6,11,8,5,11], Output = 3),
             dict(nums = [4,5,7,7,13], Output = 0),
             dict(nums = [11,6,4,8,5,9], Output = 3)]
    for test in tests:
        startTime = t.now()
        assert sol.totalSteps(test['nums']) == test['Output']
        endTime = t.now()
        print("Executed this test case: {} ms".format((endTime - startTime).total_seconds() * 1000))
        print("-----------------------------------------------------------------")