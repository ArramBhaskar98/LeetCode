from collections import deque
class Solution:
    def openLock(self, deadends, target: str) -> int:
        visited = set(deadends)
        if "0000" in visited:
            return -1
        
        que = deque()
        que.append("0000")
        steps = 0
        # abc = 0
        while len(que):
            len_que = len(que)
            for _ in range(len_que):
                curr = que.popleft()
                
                if curr == target:
                    # print('Success: ', abc)
                    return steps
                
                for i in range(4):
                    front = ""
                    back = ""
                    if curr[i] == '0':
                        front = curr[:i] + '1' + curr[i+1:]
                        back = curr[:i] + '9' + curr[i+1:]
                    elif curr[i] == '9':
                        front = curr[:i] + '0' + curr[i+1:]
                        back = curr[:i] + '8' + curr[i+1:]
                    else:
                        front = curr[:i] + chr(ord(curr[i])+1) + curr[i+1:]
                        back = curr[:i] + chr(ord(curr[i])-1) + curr[i+1:]
                    if front not in visited:
                        que.append(front)
                        visited.add(front)
                        # abc += 1
                    if back not in visited:
                        que.append(back)
                        visited.add(back)
                        # abc += 1
                    # abc += 2
            steps += 1
        # print('----', abc)
        return -1
if __name__ == '__main__':
    sol = Solution()
    tests = [dict(deadends = ["0201","0101","0102","1212","2002"], target = "0202", Output = 6),
            dict(deadends = ["8888"], target = "0009", Output = 1),
            dict(deadends = ["8887","8889","8878","8898","8788","8988","7888","9888"], target = "8888", Output = -1),
            dict(deadends = ["0000"], target = "8888", Output = -1)]
    for test in tests:
        assert sol.openLock(test['deadends'], test['target']) == test['Output']
        print('---------------------------------------------------------------')