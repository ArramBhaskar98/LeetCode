class Solution:
	def rotate(self, matrix):
		
		# Method - 1
		# m = len(matrix)
		# n = len(matrix[0])
		# arr = [[0]*n for i in range(m)]
		# k = 0
		# for i in range(m-1,-1,-1):			
		# 	j = 0
		# 	while j < n:
		# 		if k < n:
		# 			arr[j][k] = matrix[i][j]
		# 			j += 1
		# 	k += 1
		# print(arr)
		
		# Method -2 
		# for index, row in enumerate(list(map(list, zip(*matrix)))):
		# 	matrix[index] = row[::-1]
		# print(matrix)

		# Method-3
		n = len(matrix)
		for i in range(n//2):
			for j in range(i, n-1-i):
				a = matrix[i][j]
				b = matrix[j][n-1-i]
				c = matrix[n-1-i][n-1-j]
				d = matrix[n-1-j][i]

				matrix[i][j] = d
				matrix[j][n-1-i] = a
				matrix[n-1-i][n-1-j] = b
				matrix[n-1-j][i] = c
		print(matrix)

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(matrix = [[1,2,3],[4,5,6],[7,8,9]], Output = [[7,4,1],[8,5,2],[9,6,3]]),
			 dict(matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]],
			 Output = [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]),
			 dict(matrix = [[1]], Output = [[1]]),
			 dict(matrix = [[1,2],[3,4]], Output = [[3,1],[4,2]])]
	for test in tests:
		sol.rotate(test['matrix'])
		# assert sol.rotate(test['matrix']) == test['Output']
		print('----------------------------')
        