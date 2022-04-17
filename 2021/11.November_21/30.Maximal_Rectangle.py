# This problem is similar to largest rectangle in histogram.
class Solution:
    def largestRectangle(self, mat):
        res = 0
        mat.append(0)
        stack = []
        for curr_index, height in enumerate(mat):
            while stack and mat[stack[-1]] > height:
                ht = mat[stack.pop()]
                if stack:
                    ln = curr_index - stack[-1] - 1
                else:
                    ln = curr_index
                res = max(res, ln*ht)
                print(curr_index, '---', res)
            stack.append(curr_index)
            print(stack)
        print(res)
        return res

    def maximalRectangle(self, matrix) -> int:
        if not matrix:
            return 0
        rows, cols = len(matrix), len(matrix[0])
        dp = [[0]*cols for _ in range(rows)]
        for i in range(rows):
            for j in range(cols):
                if i == 0:
                    dp[i][j] = int(matrix[i][j])
                elif matrix[i][j] == '1':
                    dp[i][j] = int(matrix[i][j]) + dp[i-1][j]
        print("dp: ", dp)

        ans = 0
        for row in range(rows):
            ans = max(ans, self.largestRectangle(dp[row]))
        return ans

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]], 
                  Output = 6),
            dict(matrix = [], Output = 0),
            dict(matrix = [["0"]], Output = 0),
            dict(matrix = [["1"]], Output = 1),
            dict(matrix = [["2", "1","5","6","2","3"]], Output = 10)]
    for test in tests:
        assert sol.maximalRectangle(test['matrix']) == test['Output']
        print("----------------------------------------------------")