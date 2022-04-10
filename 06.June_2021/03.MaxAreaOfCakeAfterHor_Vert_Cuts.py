class Solution:
    def maxArea(self, h: int, w: int, horizontalCuts, verticalCuts):
        horizontalCuts.append(0)
        horizontalCuts.append(h)
        horizontalCuts.sort()
        
        verticalCuts.append(0)
        verticalCuts.append(w)
        verticalCuts.sort()
        
        m_h = 0
        for i in range(len(horizontalCuts)-1):
            h_c = horizontalCuts[i+1] - horizontalCuts[i]
            if h_c > m_h:
                m_h = h_c
        
        m_w = 0
        for i in range(len(verticalCuts)-1):
            w_c = verticalCuts[i+1] - verticalCuts[i]
            if w_c > m_w:
                m_w = w_c
        return (m_h * m_w) % (1000000007)
if __name__ == '__main__':
    sol = Solution()
    tests = [dict(h = 5, w = 4, horizontalCuts = [1,2,4], verticalCuts = [1,3], Output = 4),
            dict(h = 5, w = 4, horizontalCuts = [3,1], verticalCuts = [1], Output = 6),
            dict(h = 5, w = 4, horizontalCuts = [3], verticalCuts = [3], Output = 9)]
    for test in tests:
        assert sol.maxArea(test['h'], test['w'], test['horizontalCuts'], test['verticalCuts']) == test['Output']
        print('-------------------------------------------------------------------------------')