class Solution:
    def checkPlace(self, qarr, row, col):
        # Checking for queen present in this current column of all rows
        for i in range(row - 1, -1, -1):
            if qarr[i][col] == 'Q':
                return False

        # Checking LeftDiagonal queens present or not
        i = row - 1
        j = col - 1
        while i >= 0 and j >= 0:
            if qarr[i][j] == 'Q':
                return False
            i -= 1
            j -= 1

        # Checking RightDiagonal queens present or not
        i = row - 1
        j = col + 1
        while i >= 0 and j < self.n:
            if qarr[i][j] == 'Q':
                return False
            i -= 1
            j += 1
        return True

    def createBoard(self, qarr, row, final_lst):
        if row >= self.n:
            lst = ["".join(x) for x in qarr]
            final_lst.append(lst)
        else:
            for col in range(self.n):
                if self.checkPlace(qarr, row, col):
                    qarr[row][col] = 'Q'
                    self.createBoard(qarr, row + 1, final_lst)
                    qarr[row][col] = '.'

    def totalNQueens(self, n):
        final_lst = []
        self.n = n
        qarr = [['.'] * n for _ in range(n)]
        for i in range(n):
            qarr[0][i] = 'Q'
            self.createBoard(qarr, 1, final_lst)
            qarr[0][i] = '.'
        print('Count = ', len(final_lst))
        print(final_lst)
        return len(final_lst)

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(n=4, Output=2),
             dict(n=1, Output=1)]
    for test in tests:
        assert sol.totalNQueens(test['n']) == test['Output']
        print('--------------------------------------------')
