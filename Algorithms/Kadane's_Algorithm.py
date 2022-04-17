# Kadane's Algorithm
# For finding max sum subarray problem, Kadane's algorithm is used.
# With this Algorithm, we can able to find the best start and best end sum indices.

class Solution:
    def kadane(self, nums):
        # Method-1 without indices, just finding the max sum in a sub array
        # best_sum = curr_sum = 0
        # for num in nums:
        #     curr_sum = max(0, curr_sum+num)
        #     best_sum = max(best_sum , curr_sum)

        # return best_sum

        # Method-2 finding the start and end endices of max sub array
        best_start = best_end = 0
        best_sum = 0
        curr_sum = 0
        for curr_end, num in enumerate(nums):
            curr_sum += num         # This does cummilative sum until loop teminates 
            if curr_sum <= 0:
                curr_sum = 0
                curr_start = curr_end+1
            
            if curr_sum > best_sum:
                best_sum = curr_sum
                best_start = curr_start
                best_end = curr_end
        print(best_sum, best_start, best_end)
        return best_sum



if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [-11, 22, 33, -44, -11, 66], Output = 66),
             dict(nums = [-2,1,-3,4,-1,2,1,-5,4], Output = 6)]
    for test in tests:
        assert sol.kadane(test['nums']) == test['Output']
        print("-----------------------------------------")