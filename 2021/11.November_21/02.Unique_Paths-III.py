class Solution:
    def uniquePathsIII(self, grid) -> int:
        start, end = None, None
        visited = set()
        m = len(grid)
        n = len(grid[0])
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    visited.add((i,j))
                elif grid[i][j] == 2:
                    visited.add((i,j))
                    end = (i,j)
                elif grid[i][j] == 1:
                    start = (i,j)
        print(visited)
        def backtrack(i,j, visit):
            if (i,j) == end:
                return len(visit) == 0

            result = 0      # Always assuming that no result/way found.
            if(i,j-1) in visit:
                visit.remove((i,j-1))
                result += backtrack(i,j-1,visit)
                visit.add((i,j-1))

            if (i-1,j) in visit:
                visit.remove((i-1,j))
                result += backtrack(i-1,j,visit)
                visit.add((i-1,j))
            
            if (i,j+1) in visit:
                visit.remove((i,j+1))
                result += backtrack(i,j+1,visit)
                visit.add((i,j+1))

            if (i+1,j) in visit:
                visit.remove((i+1,j))
                result += backtrack(i+1,j,visit)
                visit.add((i+1,j))
            
            return result

        return backtrack(start[0], start[1], visited)

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(grid = [[1,0,0,0],[0,0,0,0],[0,0,2,-1]], Output = 2),
            dict(grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]], Output = 4),
            dict(grid = [[0,1],[2,0]], Output = 0)]
    for test in tests:
        assert sol.uniquePathsIII(test['grid']) == test['Output']
        print("-------------------------------------------------")