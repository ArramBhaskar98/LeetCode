class Solution:
    def allPathsSourceTarget(self, graph):
        bfs = [(0, [0])]
        answer = []
        while bfs:
            node, lst = bfs.pop(0)
            if node == len(graph)-1:
                answer.append(lst)
            else:
                for l in graph[node]:
                    bfs.append((l, lst + [l]))
        print(answer)
        return answer

if __name__ == "__main__":
    sol = Solution()
    tests = [dict(graph = [[1,2],[3],[3],[]], Output = [[0,1,3],[0,2,3]]),
            dict(graph = [[4,3,1],[3,2,4],[3],[4],[]], 
                 Output = [[0, 4], [0, 3, 4], [0, 1, 4], [0, 1, 3, 4], [0, 1, 2, 3, 4]]),
            dict(graph = [[1],[]], Output = [[0,1]]),
            dict(graph = [[1,2,3],[2],[3],[]], Output = [[0, 3], [0, 2, 3], [0, 1, 2, 3]]),
            dict(graph = [[1,3],[2],[3],[]], Output = [[0,3], [0,1,2,3]])]
    for test in tests:
        assert sol.allPathsSourceTarget(test['graph']) == test['Output']
        print("-------------------------------------------------------")