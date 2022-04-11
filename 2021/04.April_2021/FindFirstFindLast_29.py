class Solution:
    def searchRange(self, nums, target):
        if not nums:
            return [-1,-1]
        lst = []
        for index in range(len(nums)):
            if nums[index] == target:
                lst.append(index)
            else:
                continue
        if lst:
            return [lst[0], lst[-1]]
        else:
            return [-1,-1]

if __name__ == '__main__':
    sol = Solution()
    tests = [dict(nums = [5,7,7,8,8,10], target = 8, Output = [3,4]),
             dict(nums = [5,7,7,8,8,10], target = 6, Output = [-1,-1]),
             dict(nums = [], target = 0, Output = [-1,-1]),
             dict(nums = [1,5,8], target = 5, Output = [1,1])]

    for test in tests:
        assert sol.searchRange(test['nums'], test['target']) == test['Output']
        print('-----------------')
    
        