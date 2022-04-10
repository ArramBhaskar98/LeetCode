class Solution:
    def recursive(self, i, j, m, n, grid):
        if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0:
            return 0
        else:
            grid[i][j] = 0
            res = 1
            for x, y in [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]:
                res += self.recursive(x, y, m, n, grid)
            return res

    def maxAreaOfIsland(self, grid):
        m = len(grid)
        n = len(grid[0])
        ans = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    result = self.recursive(i, j, m, n, grid)
                    ans = max(result, ans)
        return ans

if __name__ == '__main__':
    sol = Solution()
    tests = [dict(grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
                          [0,0,0,0,0,0,0,1,1,1,0,0,0],
                          [0,1,1,0,1,0,0,0,0,0,0,0,0],
                          [0,1,0,0,1,1,0,0,1,0,1,0,0],
                          [0,1,0,0,1,1,0,0,1,1,1,0,0],
                          [0,0,0,0,0,0,0,0,0,0,1,0,0],
                          [0,0,0,0,0,0,0,1,1,1,0,0,0],
                          [0,0,0,0,0,0,0,1,1,0,0,0,0]], 
                          Output = 6),
            dict(grid = [[0,0,0,0,0,0,0,0]], Output = 0)]
    for test in tests:
        assert sol.maxAreaOfIsland(test['grid']) == test['Output']
        print('----------------------------------------------')