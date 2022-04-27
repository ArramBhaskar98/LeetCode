# Print the Matrix in diagonal format from bottom left to top right fashion.
class Solution:
    def findDiagonalOrder(self, mat):
        m, n = len(mat), len(mat[0])
        # Every matrix consists of m+n-1 diagonals
        diagonals = [[] for _ in range(m+n-1)]
        lst = []
        lst2 = []

        for col in range(n):
            for row in range(m-1, -1, -1):
                print("Row-Col: ", col-row)
                diagonals[abs(row+col)].append(mat[row][col])
        #         lst2.append(mat[col][row])
        #         lst.append(mat[row][col])
        # print("Lst:", lst)
        print("lst2: ", lst2)
        print("Diag: ",diagonals)

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(mat = [[1,2,3],[4,5,6],[7,8,9]], Output = [1,2,4,7,5,3,6,8,9]),
            dict(mat = [[1,2],[3,4]], Output = [1,2,3,4]),
            dict(mat = [[1,2],[2,3],[3,4]], Output = [1,2,2,3,3,4])]
    for test in tests:
        assert sol.findDiagonalOrder(test['mat']) == test['Output']
        print("--------------------------------------------------")