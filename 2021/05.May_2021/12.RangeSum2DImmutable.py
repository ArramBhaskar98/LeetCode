class NumMatrix:
	def __init__(self, matrix: List[List[int]]):
		self.mat = matrix

	def sumRegion(self, row1, col1, row2, col2):
		sumMat = 0
		for i in range(row1, row2+1):
			for j in range(col1, col2+1):
				sumMat += self.mat[i][j]
		return sumMat
                
# Your NumMatrix object will be instantiated and called as such:
if __name__ == '__main__':
	obj = NumMatrix(matrix)
	param_1 = obj.sumRegion(row1,col1,row2,col2)