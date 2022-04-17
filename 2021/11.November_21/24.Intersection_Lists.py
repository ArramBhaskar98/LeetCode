class Solution:
    def intervalIntersection(self, firstList, secondList):

        # Some Optimal Version
        ans = []
        i = j = 0
        
        while i < len(firstList) and j < len(secondList):
            lo = max(firstList[i][0], secondList[j][0])
            hi = min(firstList[i][1], secondList[j][1])
            if lo <= hi:
                ans.append([lo, hi])
            
            if firstList[i][1] < secondList[j][1]:
                i += 1
            else:
                j += 1        
        return ans
        
        # My Approach
        if not firstList or not secondList:
            return []
        answer = []

        for si, ei in firstList:
            for sj, ej in secondList:
                if sj > ei:
                    break
                elif si > ej:
                    continue
                elif si >= sj and ei <= ej:
                    answer.append([si,ei])
                elif sj >= si and ej <= ei:
                    answer.append([sj,ej])
                elif si <= ej <= ei:
                    answer.append([si,ej])
                else:
                    answer.append([sj,ei])
        return answer

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(firstList = [[0,2],[5,10],[13,23],[24,25]], 
                  secondList = [[1,5],[8,12],[15,24],[25,26]], 
                  Output = [[1,2],[5,5],[8,10],[15,23],[24,24],[25,25]]),
            dict(firstList = [[1,3],[5,9]], secondList = [], Output = []),
            dict(firstList = [], secondList = [[4,8],[10,12]], Output = []),
            dict(firstList = [[1,7]], secondList = [[3,10]], Output = [[3,7]]),
            dict(firstList = [[1,5],[6,8],[10,15],[16,25]],
                 secondList = [[0,3],[4,6],[7,12],[13,15],[16,22],[23,30]],
                 Output = [[1,3],[4,5],[6,6],[7,8],[10,12],[13,15],[16,22],[23,25]])]
    for test in tests:
        assert sol.intervalIntersection(test['firstList'], test['secondList']) == test['Output']
        print("------------------------------------------------------------------------")