class Solution:
	# This function is useful to keep queen in non-attacking positions
	def checkPlace(self, board, row, col):
		# This loop is required to check in current column no queen to be placed.
		# If any earlier row has queen it returns False
		for i in range(row - 1, -1, -1):
			if board[i][col] == 'Q':
				return False

		# This condition is, if any queen is present in top-left diagonal, return False
		i = row - 1
		j = col - 1
		while i >= 0 and j >= 0:
			if board[i][j] == 'Q':
				return False
			i -= 1
			j -= 1

		# This condition is, if any queen is present in top-right diagonal, return False
		i = row - 1
		j = col + 1
		while i >= 0 and j < self.n:
			if board[i][j] == 'Q':
				return False
			i -= 1
			j += 1

		# if none of the above conditions satisfied, return True, means current queen position
		# is safe or at non-attacking position compared to previously placed queen   
		return True

	def create(self, board, row, final_lst):
		# if row >= n means all rows successfully placed queens for current combinations so
		# place this combination in final_lst
		if row >= self.n:
			lst = ["".join(x) for x in board]
			final_lst.append(lst)
		else:
			# a- In this current row we are checking each column where queen can be placed
			for col in range(self.n):
				# For placing queen it checks the conditions as follows. If below condition is True
				if self.checkPlace(board, row, col):
					# Place the queen at current position
					board[row][col] = "Q"
					# After placing queen repeat the same process as step-a
					self.create(board, row + 1, final_lst)
					# After successful or unsuccessful placement of queen at curr position, 
					# we simply remove the queen and check for current-row next column queen 
					# placement also. 
					board[row][col] = "."

	def solveNQueens(self, n):
		self.n = n
		# Final List stores all combinations of n-queen arrangements
		final_lst = []
		board = [["."] * n for _ in range(n)]

		# This loop runs entire first row
		for i in range(n):
			# Intially placing 0th row 0th column with queen to check whether this combination is working or not
			board[0][i] = "Q"
			# After fixing board[0][0] with Queen, I'm asking to check whether at which place
			# queen is to be kept in next row
			self.create(board, 1, final_lst)
			# This step is to back-track and check all kind of combinations at first-row
			board[0][i] = "."
		print(board)
		print("Final List: ", final_lst)
		return final_lst

if __name__ == '__main__':
    sol = Solution()
    tests = [dict(n=4,
                  Output=[[".Q..", "...Q", "Q...", "..Q."], ["..Q.", "Q...", "...Q", ".Q.."]]),
             dict(n=1, Output=[["Q"]])]
    for test in tests:
        assert sol.solveNQueens(test['n']) == test['Output']
        print('---------------------------------------------')
