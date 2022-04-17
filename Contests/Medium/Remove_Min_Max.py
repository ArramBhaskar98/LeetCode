class Solution:
    def minimumDeletions(self, nums) -> int:
        n = len(nums)

        # Optimal
        i, j = nums.index(max(nums)), nums.index(min(nums))
        if i > j:
            i, j = j, i
        return min(j+1, n-i, i+1+n-j)

        # indexes
        max_index = nums.index(max(nums))
        min_index = nums.index(min(nums))

        mid = len(nums)//2

        if min_index <= mid and max_index <= mid:       # min_index and max_index both are left to mid
            return max(min_index, max_index)+1
        elif min_index >= mid and max_index >= mid:     # min_index and max_index both are right to mid
            return len(nums[min(min_index, max_index):])    
        elif min_index >= mid and max_index < mid:      # min_index is at right and max_index is at left
            return min(max_index+1 + min(min_index-max_index, n-min_index), len(nums[max_index:]))
        else:                                           # max_index is at left and min_index is at right
            return min(min_index+1 + min(max_index-min_index, n-max_index), len(nums[min_index:]))

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [2,10,7,5,4,1,8,6], Output = 5),
            dict(nums = [0,-4,19,1,8,-2,-3,5], Output = 3),
            dict(nums = [72956,-44432,78333,31358,-96449,-24776], Output = 4),
            dict(nums = [-14,61,29,-18,59,13,-67,-16,55,-57,7,74], Output = 6)]
    for test in tests:
        assert sol.minimumDeletions(test['nums']) == test['Output']
        print("--------------------------------------------------")
