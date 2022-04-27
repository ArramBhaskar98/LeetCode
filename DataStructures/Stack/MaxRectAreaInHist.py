class Solution:
    def largestRectangleArea(self, heights):
        stack = []
        ans = 0
        heights.append(0)
        dp = [0]*len(heights)   # understanding purpose
        for index, height in enumerate(heights):
            while stack and stack[-1][0] > height:
                h, pos = stack.pop()
                area = (index-pos)*h
                dp[pos] = area
                if area > ans:
                    ans = area
            stack.append((height, index))
        print(dp)
        return ans

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(heights = [2,1,5,6,2,3], Output = 10),
            dict(heights = [2,4], Output = 4)]
    for test in tests:
        assert sol.largestRectangleArea(test['heights']) == test['Output']
        print("---------------------------------------------------------")