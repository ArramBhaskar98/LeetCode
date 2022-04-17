class Solution:
    def solve(self, board):
        m = len(board)
        n = len(board[0])

        # BFS Algorithm
        def recursive(i, j):
            lst = [(i,j)]
            board[i][j] = 'D'
            while lst:
                x, y = lst.pop(0)
                for a, b in [(x,y-1),(x-1,y),(x,y+1),(x+1,y)]:
                    if 0 <= a < m and 0 <= b < n and board[a][b] == 'O':
                        board[a][b] = 'D'
                        lst.append((a,b))

        # DFS Algorithm
        def recursive(i,j):
            if 0 <= i < m and 0 <=j < n and board[i][j] == 'O':
                board[i][j] = 'D'
                recursive(i,j-1)
                recursive(i-1,j)
                recursive(i,j+1)
                recursive(i+1,j)


        for i in range(m):
            if board[i][0] == 'O':
                recursive(i, 0)
            if board[i][n-1] == 'O':
                recursive(i, n-1)
        for j in range(n):
            if board[0][j] == 'O':
                recursive(0,j)
            if board[m-1][j] == 'O':
                recursive(m-1,j)
        for i in range(m):
            for j in range(n):
                board[i][j] = 'O' if board[i][j] == 'D' else "X"
        
        return board

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
                  Output = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]),
            dict(board = [["X"]], Output = [["X"]]),
            dict(board = [["X","X","X","X"],["O","O","O","X"],["X","X","O","X"],["X","O","X","X"]],
                 Output = [["X","X","X","X"],["O","O","O","X"],["X","X","O","X"],["X","O","X","X"]])]
    for test in tests:
        assert sol.solve(test['board']) == test['Output']
        print("-----------------------------------------") 