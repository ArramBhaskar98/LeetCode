from typing import List
# Problem : https://leetcode.com/problems/contains-duplicate-ii/


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = {}
        for index in range(len(nums)):
            num = nums[index]
            if num in d and index - d[num] <= k:
                return True
            d[num] = index
        return False


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,2,3,1], k = 3, Output = True),
             dict(nums = [1,0,1,1], k = 1, Output = True),
             dict(nums = [1,2,3,1,2,3], k = 2, Output = False)]
    for test in tests:
        assert sol.containsNearbyDuplicate(test['nums'], test['k']) == test['Output'], "Test Case Failed..!"
        print("--------------------------------------------")