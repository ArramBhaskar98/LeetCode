
# Problem Statement : https://leetcode.com/problems/3sum-closest/description/

from typing import List
class Solution:
    def threeSumClosest(self, nums: List[int], target):
        nums.sort()
        cs=float('inf')
        n = len(nums)
        for i in range(n-2):
            start = i+1
            end = n-1
            while start < end:
                ts = nums[i] + nums[start] + nums[end]
                if abs(ts-target) < abs(cs-target):
                    cs=ts
                if ts < target:
                    start += 1
                elif ts > target:
                    end -= 1
                else:
                    return ts
        return cs


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [-1,2,1,-4], target = 1, Output = 2),
             dict(nums = [0,0,0], target = 1, Output = 0)]
    for test in tests:
        assert sol.threeSumClosest(test['nums'], test['target']) == test['Output']
        print("-----------------------------------------")