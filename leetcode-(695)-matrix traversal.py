class Solution(object):
    def maxAreaOfIsland(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        
        
        
        def area(i,j):
            count=0
            if i<0 or i>=height or j<0 or j>=length or grid[i][j]==0 or [i,j] in d:
                return 0
            d.append([i,j])
            count=count+1+area(i+1,j)+area(i-1,j)+area(i,j+1)+area(i,j-1)
            return count

        
        
        length=len(grid[0])
        height=len(grid)
        d=[]
        maxs=0
        for i  in range(height):
            
            for j in range(length):
                
                if grid[i][j]==1 and [i,j] not in d:
                    
                    count=area(i,j)
                    if count>maxs:
                        maxs=count
        return maxs
    
