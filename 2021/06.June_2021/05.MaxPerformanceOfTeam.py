import heapq
class Solution:
    def maxPerformance(self, n: int, speed, efficiency, k: int) -> int:
        performance = sorted(zip(efficiency, speed), key = lambda x: x[0], reverse = True)
        
        min_heap = []
        max_perf = 0
        sum_sp = 0
        
        for ef, sp in performance:
            if len(min_heap) >= k:
                # ans = sum(min_heap) * min_eff
                sum_sp -= heapq.heappop(min_heap)
                # max_perf = max(max_perf, ans)
            heapq.heappush(min_heap, sp)
            # min_eff = min(min_eff, ef)
            sum_sp += sp
            # ans = sum(min_heap) * min_eff
            max_perf = max(max_perf, sum_sp * ef)
        return max_perf % (10**9 + 7)
if __name__ == '__main__':
    sol = Solution()
    tests = [dict(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 2, Output = 60),
            dict(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 3, Output = 68),
            dict(n = 6, speed = [2,10,3,1,5,8], efficiency = [5,4,3,9,7,2], k = 4, Output = 72)]
    for test in tests:
        assert sol.maxPerformance(test['n'], test['speed'], test['efficiency'], test['k']) == test['Output']
        print('------------------------------------------------------------------------------------')