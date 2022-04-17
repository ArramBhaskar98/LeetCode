class Solution:
    def maxSubArray(self, nums):

        # Optimal Method
        cum_sum = 0
        result = nums[0]
        for num in nums:
            cum_sum += num
            if cum_sum > result:
                result = cum_sum
            if cum_sum < 0:
                cum_sum = 0
        print(result)
        return result

        # Divide and Conquer Method

        def cross(l, m, h):
            # find left max_sum before mid
            left_cum_sum = 0
            left_sum = float('-inf')
            for i in range(m, l-1, -1):
                left_cum_sum += nums[i]
                if left_cum_sum > left_sum:
                    left_sum = left_cum_sum
            
            # finding right max_sum after mid
            right_cum_sum = 0
            right_sum = float('-inf')
            for i in range(m+1, h+1):
                right_cum_sum += nums[i]
                if right_cum_sum > right_sum:
                    right_sum = right_cum_sum
            return max(left_sum+right_sum, left_sum, right_sum)

        def recursive(low, high):
            if low == high:
                return nums[low]
            mid = low + high >> 1
            
            return max(recursive(low, mid), recursive(mid+1, high), cross(low, mid, high))
        a = recursive(0, len(nums)-1)
        print(a)
        return a

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [-2,1,-3,4,-1,2,1,-5,4], Output = 6),
            dict(nums = [1], Output = 1),
            dict(nums = [5,4,-1,7,8], Output = 23)]
    for test in tests:
        assert sol.maxSubArray(test['nums']) == test['Output']
        print("---------------------------------------------")