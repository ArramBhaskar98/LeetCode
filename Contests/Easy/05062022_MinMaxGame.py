from datetime import datetime as t


class Solution:
    def minMaxGame(self, nums) -> int:
        # My Solution
        n = len(nums)
        while n > 1:
            new_nums = [0]*(n//2)
            for i in range(n//2):
                if i & 1 == 0:
                    new_nums[i] = min(nums[2 * i], nums[2 * i + 1])
                else:
                    new_nums[i] = max(nums[2 * i], nums[2 * i + 1])
            nums = new_nums
            n >>= 1
        return nums[0]


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,3,5,2,4,8,2,2], Output = 1),
             dict(nums = [3], Output = 3)]
    for test in tests:
        startTime = t.now()
        assert sol.minMaxGame(test['nums']) == test['Output']
        endTime = t.now()
        print("Executed this test case: {} ms".format((endTime-startTime).total_seconds()*1000))
        print("-----------------------------------------------------------------")