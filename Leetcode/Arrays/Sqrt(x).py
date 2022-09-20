class Solution:
    def mySqrt(self, x: int) -> int:
        if x==1 or x==2:
            return 1
        elif x==0:
            return 0
        left=0
        right=x//2
        while left<=right:
            mid=(left+right)//2
            if mid*mid==x:
                return mid
            elif mid*mid<x:
                left=mid+1
            else:
                right=mid-1
        if left>=right:
            return left-1
