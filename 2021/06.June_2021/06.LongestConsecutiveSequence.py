class Solution:
    def longestConsecutive(self, nums) -> int:
        if not nums:
            return 0
        count = 1
        ans = 1
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] == 1:
                count += 1
            elif nums[i+1] == nums[i]:
                continue
            else:
                count = 1
            ans = max(ans, count)
        return ans
if __name__ == '__main__':
    sol = Solution()
    tests = [dict(nums = [100,4,200,1,3,2], Output = 4),
            dict(nums = [0,3,7,2,5,8,4,6,0,1], Output = 9)]
    for test in tests:
        assert sol.longestConsecutive(test['nums']) == test['Output']
        print('----------------------------------------------------')