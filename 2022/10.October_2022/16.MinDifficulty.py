class Solution:
    def minDifficulty(self, jobDifficulty, d: int) -> int:



if __name__ == "__main__":
    sol = Solution()
    tests = [dict(jobDifficulty = [6,5,4,3,2,1], d = 2, Output = 7),
             dict(jobDifficulty = [9,9,9], d = 4, Output = -1),
             dict(jobDifficulty = [1,1,1], d = 3, Output = 3)]
    for test in tests:
        assert sol.minDifficulty(test['jobDifficulty'], test['d']) == test['Output'], "Test Case Failed...!"
        print("------------------------------------------------------")