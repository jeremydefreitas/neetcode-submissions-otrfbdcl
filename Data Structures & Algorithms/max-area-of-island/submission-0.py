class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visit = set()
        area = 0
        

        def bfs(r, c):
            if r not in range(ROWS) or c not in range (COLS) or (r, c) in visit or grid[r][c] == 0:
                return 0

            visit.add((r, c))
            
            return (1 + bfs(r + 1, c) + bfs(r - 1, c) + bfs(r, c + 1) + bfs(r, c - 1))
 

           
          

        maxArea = 0
        for r in range(ROWS):
            for c in range(COLS):
                maxArea = max(maxArea, bfs(r, c))
                
        return maxArea

        