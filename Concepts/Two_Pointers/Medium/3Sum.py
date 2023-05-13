
# Problem-Statement : https://leetcode.com/problems/3sum/description/

from typing import List
class Solution:
    def threeSum(self, nums: List[int]):
        # If we don't want the duplicate values in array, we need to take unique values by applying set to array.
        nums.sort()
        n = len(nums)
        result=[]
        for i in range(n-2):
            start=i+1
            end=n-1
            while start < end:
                sum3 = nums[i] + nums[start] + nums[end]
                if sum3 < 0:
                    start += 1
                elif sum3 > 0:
                    end -= 1
                else:
                    if sorted([nums[i], nums[start], nums[end]]) not in result:
                        result.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1
        print(result)
        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums=[1,2,3,-1,-2,-3], Output=[[-3,1,2],[-2,-1,3]]),
             dict(nums=[1,2,3], Output=[])]
    for test in tests:
        assert sol.threeSum(test['nums']) == test['Output']
        print("-----------------------------------------")
