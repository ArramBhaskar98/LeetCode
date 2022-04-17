class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        return str(int(num1)*int(num2))
if __name__ == "__main__":
    sol = Solution()
    tests = [dict(num1 = "2", num2 = "3", Output = "6"),
            dict(num1 = "123", num2 = "456", Output = "56088")]
    for test in tests:
        assert sol.multiply(test['num1'], test['num2']) == test['Output']
        print("--------------------------------------------------------")