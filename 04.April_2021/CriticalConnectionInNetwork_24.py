class Solution:
    def criticalConnections(self, n, connections):
    	if len(connections) == 1:
    		return connections
    	i = 0
    	while i<n:
    		if len(connections) == 1:
    			return connections
    		elif len(connections)==2 and connections[i][i+1] != connections[i+1][i]:
    			connections.pop(i)
    			print(connections)
    		elif connections[i][i+1] == connections[i+1][i] and len(connections)>2:
    			connections.pop(i)
    			print(connections)
    			i =0
    		else:
    			i
    	return connections

if __name__ == '__main__':
	sol = Solution()
	tests = [dict(n = 4, connections = [[0,1],[1,2],[2,0],[1,3]], Output = [[1,3]]),
			 dict(n = 5, connections = [[0,1],[1,2],[2,0],[1,3],[3,4]], Output = [[1,3],[3,4]])]

	for test in tests:
		assert sol.criticalConnections(test['n'], test['connections']) == test['Output']
		print('-----------------')