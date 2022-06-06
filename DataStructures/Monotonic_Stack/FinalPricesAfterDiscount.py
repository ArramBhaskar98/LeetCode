from datetime import datetime as t


class Solution:
    def finalPrices(self, prices):
        stack = []
        for i, j in enumerate(prices):
            while stack and prices[stack[-1]] >= prices[i]:
                prices[stack.pop()] -= j
            stack.append(i)
        return prices


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(prices = [8,4,6,2,3], Output = [4,2,4,2,3]),
             dict(prices = [1,2,3,4,5], Output = [1,2,3,4,5]),
             dict(prices = [10,1,1,6], Output = [9,0,1,6])]
    for test in tests:
        startTime = t.now()
        assert sol.finalPrices(test['prices']) == test['Output']
        endTime = t.now()
        print("Executed this test case: {} ms".format((endTime - startTime).total_seconds() * 1000))
        print("-----------------------------------------------------------------")