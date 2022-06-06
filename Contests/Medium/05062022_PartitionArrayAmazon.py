from datetime import datetime as t


class Solution:
    def partitionArray(self, nums, k: int) -> int:
        nums.sort()
        minElement = nums[0]
        ans = 0
        for num in nums:
            if num-minElement > k:
                minElement = num
                ans += 1
        return ans + 1

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [3,6,1,2,5], k = 2, Output = 2),
             dict(nums = [1,2,3], k = 1, Output = 2),
             dict(nums = [2,2,4,5], k = 0, Output = 3)]
    for test in tests:
        startTime = t.now()
        assert sol.partitionArray(test['nums'], test['k']) == test['Output']
        endTime = t.now()
        print("Executed this test case: {} ms".format((endTime - startTime).total_seconds() * 1000))
        print("-----------------------------------------------------------------")
