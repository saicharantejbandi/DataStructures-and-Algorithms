class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        
        def area(i,j):
            count=0
            if i<0 or i>=height or j<0 or j>=length or grid[i][j]=="0" :#or [i,j] in d:
                return 0
            grid[i][j]='0'
            #count=count+1+area(i+1,j)+area(i-1,j)+area(i,j+1)+area(i,j-1)
            
            if area(i-1,j) or area(i+1,j) or area(i,j-1) or area(i,j+1):
                return True
            else:
                return False
            
           # return count

        
        if len(grid)==0 :
            return 0
        else:
            height=len(grid)
        
        length=len(grid[0])
        
        
        k=0
        for i  in range(height):
            
            for j in range(length):
                
                if grid[i][j]=="1" :#and [i,j] not in d:
                    k=k+1
                    count=area(i,j)
                    
        
        return k
    
