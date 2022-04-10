class Solution:
    def calPoints(self, ops) -> int:
        ans = []
        for op in ops:
            if op == "C":
                ans.pop(-1)
            elif op == "D":
                ans.append(ans[-1]*2)
            elif op == "+":
                ans.append(ans[-1]+ans[-2])
            else:
                ans.append(int(op))
        return sum(ans)


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(ops = ["5","2","C","D","+"], Output = 30),
             dict(ops = ["5","-2","4","C","D","9","+","+"], Output = 27)]
    for test in tests:
        assert sol.calPoints(test['ops']) == test['Output']
        print("-------------------------------------")