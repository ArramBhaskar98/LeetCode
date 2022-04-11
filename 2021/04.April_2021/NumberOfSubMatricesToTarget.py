
def numSubMatrixSumTarget(matrix, target):
	

if __name__ == '__main__':

	tests = [dict(matrix = [[0,1,0],[1,1,1],[0,1,0]], target = 0, result = 4),
			 dict(matrix = [[1,-1],[-1,1]], target = 0, result = 5),
			 dict(matrix = [[904]], target=0, result = 0)]
	for test in tests:
		final_result = numSubMatrixSumTarget(test['matrix'], test['target'])
		print('Final Result: ', final_result)