class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        ans = [0 for _ in range(n)]
        stack = []
        for curr_day, temp in enumerate(temperatures):
            while stack and temperatures[stack[-1]] < temp:
                prev_day = stack.pop()
                ans[prev_day] = curr_day-prev_day
            stack.append(curr_day)
        return ans

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(temperatures = [73,74,75,71,69,72,76,73], Output = [1,1,4,2,1,1,0,0]),
            dict(temperatures = [30,40,50,60], Output = [1,1,1,0]),
            dict(temperatures = [30,60,90], Output = [1,1,0])]
    for test in tests:
        assert sol.dailyTemperatures(test['temperatures']) == test['Output']
        print("---------------------------------------------------------")