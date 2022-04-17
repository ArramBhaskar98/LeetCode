class Solution:
    def timeRequiredToBuy(self, tickets, k: int) -> int:
        seconds = 0
        n = len(tickets)
        while True:
            for i in range(n):
                if tickets[i] > 0:
                    tickets[i] -= 1
                    seconds += 1
                if tickets[k] == 0:
                    return seconds

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(tickets = [2,3,2], k = 2, Output = 6),
            dict(tickets = [5,1,1,1], k = 0, Output=  8),
            dict(tickets = [2,5,3,6,4,8,3,1,4,6,9,3,8,9,2,5,4,2,5,6,2,7], k = 15, Output = 82)]
    for test in tests:
        assert sol.timeRequiredToBuy(test['tickets'], test['k']) == test['Output']
        print("---------------------------------------------")