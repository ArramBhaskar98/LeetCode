class Solution:
    def singleNumber(self, nums):
        ans = set()
        for num in nums:
            if num not in ans:
                ans.add(num)
            else:
                ans.remove(num)
        return ans
if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,2,1,3,2,5], Output = [3,5]),
            dict(nums = [-1,0], Output = [-1,0]),
            dict(nums = [0,1], Output = [1,0])]
    for test in tests:
        assert sol.singleNumber(test['nums']) == test['Output']
        print("------------------------------------------------")