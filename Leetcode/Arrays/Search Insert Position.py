class Solution:
    def searchInsert(self, l: List[int], target: int) -> int:
        def modified_binary_search(l,target):
            low=0
            high=len(l)-1
            while low<=high:
                mid=(low+high)//2
                if l[mid]==target:
                    return mid
                    break
                elif l[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
            else:
                return low
        return modified_binary_search(l,target)
