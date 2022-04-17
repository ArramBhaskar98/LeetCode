class Solution:
    def largestDivisibleSubset(self, nums):
        nums.sort()
        dp = [[num] for num in nums]
        for i in range(len(nums)):
            for j in range(i):
                if nums[i] % nums[j] == 0 and len(dp[j])+1 > len(dp[i]):
                    dp[i] = dp[j] + [nums[i]]
        print(dp)
        return max(dp, key=len)

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,2,3], Output = [1,2]),
            dict(nums = [1,2,4,8], Output = [1,2,4,8]),
            dict(nums = [4,8,10,240], Output = [4,8,240])]
    for test in tests:
        assert sol.largestDivisibleSubset(test['nums']) == test['Output']
        print("-------------------------------------------------------")