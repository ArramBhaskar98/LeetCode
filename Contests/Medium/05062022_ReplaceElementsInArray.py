from datetime import datetime as t


class Solution:
    def arrayChange(self, nums, operations):
        d1 = {}
        d2 = {}
        for i in range(len(nums)):
            d1[nums[i]] = i
            d2[i] = nums[i]
        for op1, op2 in operations:
            if op1 in d1:
                d1[op2]=d1[op1]
                del d1[op1]
                d2[d1[op2]] = op2   # or d2[d1[op1]]=op2
        return [val for ind, val in d2.items()]


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [1,2,4,6], operations = [[1,3],[4,7],[6,1]], Output = [3,2,7,1]),
             dict(nums = [1,2], operations = [[1,3],[2,1],[3,2]], Output = [2,1])]
    for test in tests:
        startTime = t.now()
        assert sol.arrayChange(test['nums'], test['operations']) == test['Output']
        endTime = t.now()
        print("Executed this test case: {} ms".format((endTime - startTime).total_seconds() * 1000))
        print("-----------------------------------------------------------------")