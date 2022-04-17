from collections import Counter


class Solution:
    def minimumRounds(self, tasks) -> int:
        ans = 0
        d = Counter(tasks)
        for i in d.values():
            if i <= 1:
                return -1
            this_round = i // 3
            if i%3 != 0:
                this_round += 1
            ans += this_round
        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [dict(tasks = [2,2,3,3,2,4,4,4,4,4], Output = 4),
             dict(tasks = [2,3,3], Output = -1),
             dict(tasks = [69,65,62,64,70,68,69,67,60,65,69,62,65,65,61,66,68,61,65,63,60,66,68,66,67,65,63,65,70,69,70,62,68,70,60,68,65,61,64,65,63,62,62,62,67,62,62,61,66,69], Output = 20)]
    for test in tests:
        assert  sol.minimumRounds(test['tasks']) == test['Output']
        print("-------------------------------------------------")
