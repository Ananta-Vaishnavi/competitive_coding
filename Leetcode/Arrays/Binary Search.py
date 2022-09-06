class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def BinarySearch(nums,target):
            start=0
            end=len(nums)-1
            while end>=start:
                mid=(start+end)//2
                if nums[mid]==target:
                    return mid
                elif nums[mid]>target:
                    end=mid-1
                else:
                    start=mid+1
            if end<=start:
                return -1
        return BinarySearch(nums,target)
        
