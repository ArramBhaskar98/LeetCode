class Solution:
    def findKthNumber(self, m: int, n: int, k: int) -> int:
        if m > n:
            m, n = n, m
        if m*n == k:
            return k
        lo, hi = 1, m*n

        while lo < hi:
            mid = lo+hi >> 1
            if sum(min(mid //i, n) for i in range(1, m+1)) < k:
                lo = mid + 1
            else:
                hi = mid
        return lo

        # Store the data in list
        # Brute-Force
        mat = [i*j for i in range(1, m+1) for j in range(1, n+1)]
        mat.sort()
        return mat[k-1]
        
        # My Approach
        mat = [[0]*n for _ in range(m)]
        lst = []
        for i in range(m):
            for j in range(n):                
                mat[i][j] = (i+1)*(j+1)
                bisect.insort_left(lst, mat[i][j])
        return lst[k-1]


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(m = 3, n = 3, k = 5, Output = 3),
            dict(m = 2, n = 3, k = 6, Output = 6),
            dict(m = 9895, n = 28405, k = 100787757, Output = 31666344)]
    for test in tests:
        assert sol.findKthNumber(test['m'], test['n'], test['k']) == test['Output']
        print("----------------------------------------------------------------")