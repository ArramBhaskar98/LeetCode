class Solution:
    def findDiagonalOrder(self, mat):

        # Time Complexity is O(n.m)
        # The Pattern followed for this Matrix filling is
        #  ^ ^ ^
        # / / /
        #/ / /
        # Reference for this problem https://leetcode.com/problems/diagonal-traverse/
        # https://leetcode.com/submissions/detail/588519385/
        
        m, n = len(mat), len(mat[0])
        diagonals = [[] for _ in range(m+n-1)]

        # Fill the diagonal elements of mat in respective diagonals
        for i in range(m):
            for j in range(n):
                diagonals[i+j].append(mat[i][j])
        print(diagonals)

        answer = []
        for index, sub_mat in enumerate(diagonals):
            if index % 2 == 0:
                for sub in sub_mat[::-1]:
                    answer.append(sub)
            else:
                for sub in sub_mat:
                    answer.append(sub)
        print(answer)
        return answer

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(mat = [[1,2,3],[4,5,6],[7,8,9]], Output = [1,2,4,7,5,3,6,8,9]),
            dict(mat = [[1,2],[3,4]], Output = [1,2,3,4]),
            dict(mat = [[1,2],[2,3],[3,4]], Output = [1,2,2,3,3,4])]
    for test in tests:
        assert sol.findDiagonalOrder(test['mat']) == test['Output']
        print("--------------------------------------------------")