class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def floor(matrix,target):
            left=0
            res=0
            right=len(matrix)-1
            while left<=right:
                mid=(left+right)//2
                if matrix[mid][0]==target:
                    return mid
                elif matrix[mid][0]<target:
                    res=mid
                    left=mid+1 
                else:
                    right=mid-1
            return res
        a=floor(matrix,target)
        #print(a)
        def BinarySearch(matrix,target,a):
            left=0
            right=len(matrix[0])-1
            while left<=right:
                mid=(left+right)//2
                if matrix[a][mid]==target:
                    print(mid)
                    return True
                elif matrix[a][mid]<target:
                    left=mid+1 
                else:
                    right=mid-1
            if left>=right:
                return False
        return BinarySearch (matrix,target,a)
