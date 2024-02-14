class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        numOfCities = len(isConnected)
        visited = [False] * numOfCities
        numOfProvinces = 0

        def dfs(nodeId):
            visited[nodeId] = True
            
            for adjacent in range(numOfCities):
                if visited[adjacent] == False and isConnected[nodeId][adjacent]== 1:
                    dfs(adjacent)
        

        for i in range(numOfCities):
            if not visited[i]:
                numOfProvinces += 1
                dfs(i)
                
        return numOfProvinces
        