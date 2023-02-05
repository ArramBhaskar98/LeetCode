class Solution:
    def largestPerimeter(self, nums) -> int:
        nums.sort(reverse = True)
        for i in range(len(nums)-2):
            if nums[i+1] + nums[i+2] > nums[i]:
                return nums[i+1] + nums[i+2] + nums[i]
        return 0


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [2,1,2], Output = 5),
             dict(nums = [1,2,1], Output = 0)]
    for test in tests:
        assert sol.largestPerimeter(test['nums']) == test['Output']
        print("----------------------------------")