from math import comb
class Solution:
    def numTrees(self, n: int) -> int:
        return int((1/(n+1))*comb(2*n,n))

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(n = 3, Output = 5),
            dict(n = 1, Output = 1)]
    for test in tests:
        assert sol.numTrees(test['n']) == test['Output']
        print("---------------------------------------")