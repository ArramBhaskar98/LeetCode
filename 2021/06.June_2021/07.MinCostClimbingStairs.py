class Solution:
    def minCostClimbingStairs(self, cost) -> int:
        def minCost(i):
            if i <= 1:
                return 0
            if i in d:
                return d[i]
            d[i] = min(cost[i-1] + minCost(i-1), cost[i-2] + minCost(i-2))
            return d[i]
        
        d = {}
        return minCost(len(cost))
if __name__ == '__main__':
    sol = Solution()
    tests = [dict(cost = [10,15,20], Output = 15),
            dict(cost = [1,100,1,1,1,100,1,1,100,1], Output = 6)]
    for test in tests:
        assert sol.minCostClimbingStairs(test['cost']) == test['Output']
        print('----------------------------------------------------------')