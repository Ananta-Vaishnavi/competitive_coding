class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        def path(grid,i,j,m,n):
            if (i==m-1 and j==n-1):
                return grid[i][j]
            if i==m or j==n:
                return 1000000
            if temp[i][j]!=-1:
                return temp[i][j]
            temp[i][j]=grid[i][j]+min((path(grid,i+1,j,m,n)),(path(grid,i,j+1,m,n)))
            return temp[i][j]
        
        m,n=len(grid),len(grid[0])
        temp = [[-1 for i in range(n)] for j in range(m)]
        return path(grid,0,0,m,n)
