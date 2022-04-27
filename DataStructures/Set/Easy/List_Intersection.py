class Solution:
    def intersection(self, nums):

        # Method - 1
        a = set(nums[0]).intersection(*nums[1:])
        return sorted(a)

        # Method - 2
        a = nums[0]
        for lst in nums[1:]:
            b = set(a).intersection(lst)
            a = b
        print(a)
        return list(a)


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [[3,1,2,4,5],[1,2,3,4],[3,4,5,6]], Output = [3,4]),
             dict(nums = [[1,2,3],[4,5,6]], Output = [])]
    for test in tests:
        assert  sol.intersection(test['nums']) == test['Output']
        print("-----------------------------------------------")