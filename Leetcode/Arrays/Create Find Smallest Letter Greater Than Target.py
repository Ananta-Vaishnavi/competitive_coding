class Solution:
    def nextGreatestLetter(self, a: List[str], target: str) -> str:
        a=list(set(a))
        a.sort()
        def BinarySearch(a,target):
            left=0
            right=len(a)-1
            res=a[right]
            while left<=right:
                mid=(left+right)//2
                if ord(a[mid])==ord(target):
                    return a[mid+1]
                elif ord(a[mid])<ord(target):
                    left=mid+1
                else:
                    right=mid-1
                    res=a[mid]
            return res
        if ord(a[-1])<=ord(target):
            return a[0]
        else:
            return BinarySearch(a,target)
