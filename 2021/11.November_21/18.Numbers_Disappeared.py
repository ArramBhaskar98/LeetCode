class Solution:
    def findDisappearedNumbers(self, nums):
        
        # Method-1 Set Difference.
        return set(range(1, len(nums)+1))-set(nums)

        # # Method-2 Regular Approach
        n = len(nums)
        answer = set()        
        for i in range(1, n+1):
            answer.add(i)
        a = answer.difference(nums)
        print(a)
        return a

        # Method-3
        n = len(nums)
        nums = set(nums)
        result = []
        for i in range(1, n+1):
            if i not in nums:
                result.append(i)
        return result

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [4,3,2,7,8,2,3,1], Output = [5,6]),
            dict(nums = [1,1],Output = [2])]
    for test in tests:
        assert sol.findDisappearedNumbers(test['nums']) == test['Output']
        print("------------------------------------------------------")