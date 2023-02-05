from typing import List
# Problem : https://leetcode.com/problems/continuous-subarray-sum/
# Best Explanation : https://www.youtube.com/watch?v=OKcrLfR-8mE
""" This problem can be solved using Dictionary. In General this problem is related to Math Logic
* We keep on adding each element to total and keep on checking for the remainder for running sum is divisible by k.
* If the remainder is not in dictionary, we add that remainder with index (till current sum)
* If the same remainder again found in dictionary, it means that our current index - remainder of index > 1
  gives SubArraySum (excluding nums value of remainder of index)."""


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = {0:-1}      # here 0 index is required, because 0 also a valid integer multiples of k.
        total = 0
        for i in range(len(nums)):
            total += nums[i]
            remainder = total % k
            if remainder in d:
                value = d[remainder]
                if i - value > 1:
                    return True
            else:
                d[remainder] = i
        return False


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [23,2,4,6,7], k = 6, Output = True),
             dict(nums = [23,2,6,4,7], k = 6, Output = True),
             dict(nums = [23,2,6,4,7], k = 13, Output = False),
             dict(nums = [20,1,1], k = 6, Output = False),
             dict(nums = [18,0,0], k = 6, Output = True),
             dict(nums = [23,0,0], k = 6, Output = True),
             dict(nums = [25,0,1], k = 6, Output = False)]
    for test in tests:
        assert sol.checkSubarraySum(test['nums'], test['k']) == test['Output'], "Test Case Failed...!"
        print("----------------------------------------------")