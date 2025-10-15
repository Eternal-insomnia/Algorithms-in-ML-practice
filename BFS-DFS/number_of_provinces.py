class Solution:
    def go_deeper(self, isConnected: List[List[int]], j: int, visited: set):
        count = 1
        visited.add(j)
        for k in range(len(isConnected)):
            if k == j or k in visited:
                continue
            elif isConnected[k][j] == 1:
                self.go_deeper(isConnected, k, visited)

    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected) # rows and cols
        visited = set()
        provinces_count = 0

        for i in range(n):
            for j in range(i, n):
                if isConnected[i][j] == 0 or j in visited:
                    continue
                self.go_deeper(isConnected, j, visited)
                provinces_count += 1
        return provinces_count
