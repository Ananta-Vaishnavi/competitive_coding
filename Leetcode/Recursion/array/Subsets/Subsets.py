class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def sol(i):
            if i >= len(nums):
                ans.append(op.copy())
                return   
            sol(i+1)
            op.append(nums[i])
            sol(i+1)
        ans = []
        op = []
        sol(0)
        return ans
