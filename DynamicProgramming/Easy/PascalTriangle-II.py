class Solution:
    def getRow(self, rowIndex: int):

        # Short Method
        # row = [1]
        # for i in range(rowIndex):
        #     for j in range(i, 0, -1):
        #         row[j] = row[j] + row[j-1]
        #     row.append(1)
        # return row

        # My Method
        lst = [[1]*i for i in range(1,rowIndex+2)]
        if rowIndex < 2:
            return lst[rowIndex]
        for i in range(2, len(lst)):
            for j in range(1, len(lst[i])-1):
                lst[i][j] = lst[i-1][j-1]+lst[i-1][j]
        return lst[-1]

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(rowIndex = 3, Output = [1,3,3,1]),
            dict(rowIndex = 0, Output = [1]),
            dict(rowIndex = 1, Output = [1,1])]
    for test in tests:
        assert sol.getRow(test['rowIndex']) == test['Output']
        print('--------------------------------------------')