from collections import defaultdict
# Problem-Statement : https://leetcode.com/problems/3sum/description/

from typing import List
class Solution:
    def threeSum(self, nums: List[int]):
        # If we don't want the duplicate values in array, we need to take unique values by applying set to array.
        nums.sort()
        n = len(nums)
        result=[]
        for i in range(n-2):
            T = nums[i]
            d = defaultdict(list)
            for j in range(i+1,n-1):
                d[T+nums[j]].append([T, nums[j]])
                if d[nums[j]]

        print(result)
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums=[1,2,3,-1,-2,-3], Output=[[-3,1,2],[-2,-1,3]]),
             dict(nums=[1,2,3], Output=[])]
    for test in tests:
        assert sol.threeSum(test['nums']) == test['Output']
        print("-----------------------------------------")
