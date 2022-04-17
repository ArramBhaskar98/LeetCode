class Solution:
    def maxProfit(self, prices) -> int:
        profit = 0
        for i in range(1, len(prices)):
            if prices[i] > prices[i-1]:
                profit +=  prices[i]-prices[i-1]
        return profit

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(prices = [7,1,5,3,6,4], Output = 7),
            dict(prices = [1,2,3,4,5], Output = 4),
            dict(prices = [7,6,4,3,1], Output = 0)]
    for test in tests:
        assert sol.maxProfit(test['prices']) == test['Output']
        print("----------------------------------------------")