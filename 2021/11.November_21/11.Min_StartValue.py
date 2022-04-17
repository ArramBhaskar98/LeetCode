class Solution:
    def minStartValue(self, nums) -> int:

        # One Pass Solution -- O(n)
        startVal = 0
        cumSum = 0
        for num in nums:
            cumSum += num
            startVal = min(startVal, cumSum)
        return -startVal + 1

        # BruteForce--O(n**k * m)
        startVal = 1
        while True:
            cumSum = startVal
            flag = 1
            for num in nums:
                cumSum += num
                if cumSum < 1:
                    flag = 0
                    break
            if flag == 1:
                return startVal
            startVal += 1

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(nums = [-3,2,-3,4,2], Output = 5),
            dict(nums = [1,2], Output = 1),
            dict(nums = [1,-2,-3], Output = 5)]
    for test in tests:
        assert sol.minStartValue(test['nums']) == test['Output']
        print("-----------------------------------------------")