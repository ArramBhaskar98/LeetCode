class Solution:
    def rob(self, nums) -> int:
        if len(nums) <= 2:
            return max(nums)
        n = len(nums)
        nums[2] += nums[0]
        for i in range(3, n):
            nums[i] += max(nums[i-2], nums[i-3])
        return max(nums[-1], nums[-2])

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,2,3,1], Output = 4),
            dict(nums = [2,7,9,3,1], Output = 12),
            dict(nums = [2,1,1,2], Output = 4)]
    for test in tests:
        assert sol.rob(test['nums']) == test['Output']
        print("-------------------------------------")