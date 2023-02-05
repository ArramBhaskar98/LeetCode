class Solution:
    def increasingTriplet(self, nums) -> bool:
        min1, min2 = float('inf'), float('inf')
        for num in nums:
            if num <= min1:
                min1 = num
            elif num <= min2:
                min2 = num
            else:
                return True
        return False


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,2,3,4,5], Output = True),
             dict(nums = [5,4,3,2,1], Output = False),
             dict(nums = [2,1,5,0,4,6], Output = True)]
    for test in tests:
        assert sol.increasingTriplet(test['nums']) == test['Output'], "Test Case Failed....!"
        print("---------------------------")