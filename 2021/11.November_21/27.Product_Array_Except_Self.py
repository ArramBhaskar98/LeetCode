class Solution:
    def productExceptSelf(self, nums):
        n = len(nums)
        product = 1
        zeros = 0
        for num in nums:
            if num != 0:
                product *= num
            else:
                zeros += 1
        if zeros > 1:
            return [0]*n
        for i in range(n):
            if zeros:
                if nums[i] == 0:
                    nums[i] = product
                else:
                    nums[i] = 0
            else:
                nums[i] = product//nums[i]
        
        return nums

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,2,3,4], Output = [24,12,8,6]),
            dict(nums = [-1,1,0,-3,3], Output = [0,0,9,0,0]),
            dict(nums = [0,0,2], Output = [0,0,0])]
    for test in tests:
        assert sol.productExceptSelf(test['nums']) == test['Output']
        print("----------------------------------------------------")