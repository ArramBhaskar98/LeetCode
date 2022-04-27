class Solution:
    def singleNonDuplicate(self, nums) -> int:

        # Binary Search- O(logn)
        lo, hi = 0, len(nums) - 1
        while lo < hi:
            mid = lo + hi >> 1
            if mid % 2 == 1:
                mid -= 1
            if nums[mid] == nums[mid + 1]:
                lo = mid + 2
            else:
                hi = mid
        return nums[lo]

        # Normal Approach - O(n)
        ans = []
        for num in nums:
            if num not in ans:
                ans.append(num)
            else:
                ans.remove(num)
        return ans[0]


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8], Output=2),
             dict(nums=[3, 3, 7, 7, 10, 11, 11], Output=10)]
    for test in tests:
        assert sol.singleNonDuplicate(test['nums']) == test['Output']
        print("----------------------------------------------------")
