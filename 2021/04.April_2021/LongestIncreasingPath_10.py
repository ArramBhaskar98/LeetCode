#longestincreasingPath is called by sending a matrix
#To find the longest path the longest path from each index has to be found then only we can decide it is the longest path
#hence an empty matrix "mat" with all zeros is created of same size of given input matrix (i.e, to store longest path at each index) 
# then recursive function is called for each index of input matix
# Recursive function defined as
# it checks whether the longest path at that index is not present in the mat
# if not present then(here if not present only code is executed and if it is present in mat no need of further computation directly mat is returned(which saves time))
#---adjacent_paths is created empty(which is capable of storing the adjacent indices longest paths)
#--- then for each adjacent index(i.e,left,top,right,bottom) is checked with
#		Whether adjacent is not out of bound and adjacent is greater value 
#		if satisfies above condition then the adjacent_paths list is appended with longest_path from the adjacent index 
#		by using same recusrive function
#	after that the max of adjacent paths is found and by using max function(here 1 is added since current index is also counted in the path)
#after that the mat is returned at the end
#the max function is applied for recurisive function calls in the begining which results the max value of the returned mat
def longestIncreasingPath(matrix):
	if not matrix:
		return 0
	m = len(matrix)
	n = len(matrix[0])

	mat = [[0]*n for _ in range(m)]

	def recursive(i,j):
		if not mat[i][j]:
			adjacent_paths = []
			for x,y in ((i, j-1), (i-1,j), (i, j+1), (i+1,j)):
				if 0<=x<m and 0<=y<n and matrix[x][y] > matrix[i][j]:
					adjacent_paths.append(recursive(x, y))
			mat[i][j] = 1 + max(adjacent_paths, default=0)
			print(mat)
		return mat[i][j]

	return max(recursive(i,j) for i in range(m) for j in range(n))

if __name__ == '__main__':
	tests = [
			 dict(matrix = [[3,4,5],[3,2,6],[2,2,1]], result = 4),
			 dict(matrix = [[9,9,4],[6,6,8],[2,1,1]], result = 4),
			 dict(matrix = [[1]], result = 1)]
	for test in tests:
		assert longestIncreasingPath(test['matrix']) == test['result']
		# result = longestIncreasingPath(test['matrix'])
		print('------------------------------------')