class Solution:
    def maximumUniqueSubarray(self, nums):
        ans = curr_sum = i = 0
        seen = set()
        for j in range(len(nums)):
            while nums[j] in seen:
                seen.remove(nums[i])
                curr_sum -= nums[i]
                i += 1
            seen.add(nums[j])
            curr_sum += nums[j]
            ans = max(ans, curr_sum)
        return ans

if __name__ == '__main__':
    sol = Solution()
    tests = [
        dict(nums = [4,2,4,5,6], Output = 17),
        dict(nums = [5,2,1,2,5,2,1,2,5], Output = 8),
        dict(nums=[888, 4893, 99, 748, 4893, 888, 484, 748, 3984, 844], Output=11841)]
    for test in tests:
        assert sol.maximumUniqueSubarray(test['nums']) == test['Output']
        print('-------------------------------------------------')
