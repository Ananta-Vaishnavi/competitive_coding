class Solution:
    def convertToWave(self, n : int, a : List[int]) -> None:
        left=0
        right=1
        while right<n:
            a[right],a[left]=a[left],a[right]
            right+=2
            left+=2
        return a
