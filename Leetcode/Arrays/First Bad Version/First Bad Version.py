# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        left = 1
        right = n

        if n == 0 or n == 1:
            return n
        res = n//2
        while left <= right:
            mid = (left + right)//2
            if isBadVersion(mid):
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
