class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        def subsets(i=0, op=[]):
            if i == len(nums):
                res.append(op[:])
                return 

            op.append(nums[i])
            subsets(i+1, op)
            op.pop()
            while i+1 < len(nums) and nums[i] == nums[i+1]:
                i+=1
            subsets(i+1, op) 

        subsets()
        return res
