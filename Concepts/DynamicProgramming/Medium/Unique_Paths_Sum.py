class Solution:
    def minPathSum(self, grid) -> int:
        m = len(grid)
        n = len(grid[0])

        # Firstly doing sum along all the Rows of 1st Column 
        for i in range(1, m):
            grid[i][0] += grid[i-1][0]
        
        # Doing sum along all Columns of 1st Row
        for i in range(1, n):
            grid[0][i] += grid[0][i-1]

        # Finding which number gives minimum sum from previous left and previous top position
        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i-1][j], grid[i][j-1])
        return grid[-1][-1]

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(grid = [[1,3,1],[1,5,1],[4,2,1]], Output = 7),
            dict(grid = [[1,2,3],[4,5,6]], Output = 12)]
    for test in tests:
        assert sol.minPathSum(test['grid']) == test['Output']
        print("--------------------------------------------")