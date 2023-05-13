
class Solution:
    def hcf(self, a, b):
        if a == b:
            return a
        while b:
            temp = b
            b = a % b
            a = temp
        return a
    
    def lcm(self, a, b):
        return (a*b)//self.hcf(a,b)

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(a = 15, b = 20, Output = 60),
            dict(a = 14, b = 7, Output = 14),
            dict(a = 3, b = 7, Output = 21)]
    for test in tests:
        assert sol.lcm(test['a'], test['b']) == test['Output']
        print("----------------------------------------------")
