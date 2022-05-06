class Solution:
    def minimumGroups(self, awards, k):
        """ The main aim of the program is to divide the awards in groups such that difference in the number of
        awards won by any two movies in that group should not exceed the k."""
        ans = 0
        awards.sort()
        minimum = awards[0]
        for num in awards[1:]:
            if abs(num - minimum) > k:
                minimum = num
                ans += 1
        return ans + 1


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(awards=[3, 1, 3, 5, 9], k=10, Output=1),
             dict(awards=[1, 13, 6, 8, 9, 3, 5], k=4, Output=3),
             dict(awards=[1, 5, 4, 6, 8, 9, 2], k=3, Output=3)]
    for test in tests:
        sol.minimumGroups(test['awards'], test['k']) == test['Output']
        print("------------------------------------------")
