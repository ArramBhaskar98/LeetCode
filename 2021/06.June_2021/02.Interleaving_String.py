from functools import lru_cache
class Solution:
    @lru_cache()
    def recursive(self, s1, s2, s3, i, j, k):
        if i < len(s1) and j < len(s2) and s3[k] != s1[i] and s3[k] != s2[j]:
            return False
        if k == len(s3):
            return True     

        res = False

        if i < len(s1) and s3[k] == s1[i]:
            res = self.recursive(s1, s2, s3, i+1, j, k+1)
        if j < len(s2) and s3[k] == s2[j]:
            res = res or self.recursive(s1, s2, s3, i, j+1, k+1)

        return res


    def isInterleave(self, s1, s2, s3):
        if not s1 and not s2 and not s3:
            return True
        if len(s1) + len(s2) != len(s3):
            return False
        res = self.recursive(s1, s2, s3, 0, 0, 0)
        return res

if __name__ == '__main__':
    sol = Solution()
    tests = [dict(s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc", Output = False),
            dict(s1 = "", s2 = "", s3 = "", Output = True)]
    for test in tests:
        assert sol.isInterleave(test['s1'], test['s2'], test['s3']) == test['Output']
        print('--------------------------------------------------------------------')
