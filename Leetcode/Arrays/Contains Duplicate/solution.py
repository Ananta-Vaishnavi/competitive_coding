class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        c=0
#First we arrange the numbers in order and then we check if there the subsequent numbers are same
        nums.sort()
        for i in range(len(nums)-1):
            if nums[i]==nums[i+1]:
                c=1
                return 'true'
                break
                
        if c==1:
            return 'false'
            
