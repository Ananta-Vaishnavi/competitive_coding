class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans=[]
        def combination(sum,comb):
            if sum == target:
                    comb.sort()
                    if comb not in ans:
                        ans.append(comb.copy())
                    return 
            for i in range(0,len(candidates)):
                if sum + candidates[i] <= target:
                    combination(sum+candidates[i],comb+[candidates[i]])
        combination(0,[])
        return ans


