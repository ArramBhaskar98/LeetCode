class Solution:
    def shiftGrid(self, grid, k: int):
        m = len(grid)
        n = len(grid[0])
        vector = [0] * m * n
        k = k % (m * n)
        for i in range(m):
            for j in range(n):
                vector[i * n + j] = grid[i][j]

        final_vec = vector[-k:] + vector[:-k]

        for i in range(m):
            for j in range(n):
                grid[i][j] = final_vec[i * n + j]
        return grid


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 1, Output = [[9,1,2],[3,4,5],[6,7,8]]),
             dict(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4, Output = [[12,0,21,13],[3,8,1,9],[19,7,2,5],[4,6,11,10]]),
             (dict(grid = [[1,2,3],[4,5,6],[7,8,9]], k = 9, Output = [[1,2,3],[4,5,6],[7,8,9]]))]
    for test in tests:
        assert sol.shiftGrid(test['grid'], test['k']) == test['Output']
        print("-------------------------------------")