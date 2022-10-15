class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        index={}
        for i in range(len(nums)):
            if nums[i] in index:
                index[nums[i]].append(i)
            else:
                index[nums[i]]=[i]
        maxf=0
        for i in index.values():
            maxf=max(maxf,len(i))
        min_i=len(nums)
        for i in index.values():
            if len(i)==maxf:
                min_i=min(min_i,(i[-1]-i[0])+1)
        return min_i
        
