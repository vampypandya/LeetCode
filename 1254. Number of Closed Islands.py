class Solution(object):
    def closedIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        visited = []
        island = 0
        
        def go_island(x,y):
            if(x==0 or x == len(grid)-1 or y==0 or y == len(grid[0])-1):
                return False
            if(grid[x][y] == 0):
                # print grid
                grid[x][y] = "#"
                if(x+1<len(grid) and grid[x+1][y] == 0):
                    if(not go_island(x+1,y)):
                        grid[x][y] = 0
                        return False
                if(y+1<len(grid[0]) and grid[x][y+1] == 0):
                    if(not go_island(x,y+1)):
                        grid[x][y] = 0
                        return False
                if(x-1>=0 and grid[x-1][y] == 0):
                    if(not go_island(x-1,y)):
                        grid[x][y] = 0
                        return False
                if(y-1>=0 and grid[x][y-1] == 0):
                    if(not go_island(x,y-1)):
                        grid[x][y] = 0
                        return False
                return True
            return False
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if(go_island(i,j)):
                    # print i,j
                    island = island + 1
        
        return island
