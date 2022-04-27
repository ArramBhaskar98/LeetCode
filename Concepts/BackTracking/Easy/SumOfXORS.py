from itertools import combinations
from functools import reduce
class Solution:
    def subsetXORSum(self, nums) -> int:
        # My Method
        total = sum(nums)
        for x in range(2, len(nums)+1):
            comb = list(combinations(nums, x))

            for tup in comb:
                total += reduce(lambda x,y: x^y, tup)
        return total
        
        # Short Method
        or_bits = 0
        for i in nums:
            or_bits |=i
            print(or_bits)
        return or_bits * 2**(len(nums)-1)

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,3], Output = 6),
            dict(nums = [5,1,6], Output = 28),
            dict(nums = [3,4,5,6,7,8], Output = 480)]
    for test in tests:
        assert sol.subsetXORSum(test['nums']) == test['Output']
        print('----------------------------------------------')