class Solution:
   
    def getTotalIsles(self, grid: list[list[str]]) -> int:
    #    write your code here
        if not grid:
            return 0
            
        rows = len(grid)
        cols = len(grid[0])
        islands = 0
        
        def dfs(i: int, j: int) -> None:
            # Check if current position is out of bounds or not land
            if (i < 0 or i >= rows or 
                j < 0 or j >= cols or 
                grid[i][j] != '1'):
                return
            
            # Mark current land as visited by changing it to '2'
            grid[i][j] = '2'
            
            # Check all adjacent cells
            dfs(i+1, j)  # down
            dfs(i-1, j)  # up
            dfs(i, j+1)  # right
            dfs(i, j-1)  # left
        
        # Iterate through each cell in the grid
        for i in range(rows):
            for j in range(cols):
                # If we find a new unvisited island (1)
                if grid[i][j] == '1':
                    islands += 1
                    # Use DFS to mark all connected land
                    dfs(i, j)
        
        # Restore grid to original state (optional)
        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == '2':
                    grid[i][j] = '1'
                    
        return islands
