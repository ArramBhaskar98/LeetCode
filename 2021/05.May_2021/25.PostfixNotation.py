class Solution:
	def evalRPN(self, tokens):
		stack = []
		for item in tokens:
			if item == '+':
				stack.append(stack.pop(-2) + stack.pop(-1))
			elif item == '-':
				stack.append(stack.pop(-2) - stack.pop(-1))
			elif item == '*':
				stack.append(stack.pop(-2) * stack.pop(-1))
			elif item == '/':
				stack.append(int(stack.pop(-2) / stack.pop(-1)))
			else:
				stack.append(int(item))
		print('List: ', stack)
		return stack[0]

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(tokens = ["2","1","+","3","*"], Output = 9),
			dict(tokens = ["4","13","5","/","+"], Output = 6),
			dict(tokens = ["10","6","9","3","+","-11","*","/","*","17","+","5","+"], Output = 22)]
	for test in tests:
		assert sol.evalRPN(test['tokens']) == test['Output']
		print('--------------------------------')
