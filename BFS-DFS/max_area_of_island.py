class Solution:
    def go_deeper(self, grid: List[List[int]], i: int, j: int, visited: set) -> int:
        if grid[i][j] == 0:
            return 0
        count = 1
        visited.add((i, j))
        if i-1 >= 0 and (i-1, j) not in visited:
            count += self.go_deeper(grid, i-1, j, visited)
        if j+1 < len(grid[i]) and (i, j+1) not in visited:
            count += self.go_deeper(grid, i, j+1, visited)
        if i+1 < len(grid) and (i+1, j) not in visited:
            count += self.go_deeper(grid, i+1, j, visited)
        if j-1 >= 0 and (i, j-1) not in visited:
            count += self.go_deeper(grid, i, j-1, visited)
        return count

    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid) # rows
        n = len(grid[0]) # cols
        visited = set()
        max_square = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0 or (i, j) in visited:
                    continue
                square = self.go_deeper(grid, i, j, visited)
                if square > max_square:
                    max_square = square

        return max_square
