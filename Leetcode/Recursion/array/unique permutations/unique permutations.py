class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = [] #[]
        count={} #{1: 1, }
        for i in nums:
            if i in count:
                count[i] += 1 
            else:
                count[i] = 1 
        def backtracking(count,perm):
            if len(perm) == len(nums):
                res.append(perm[::])
                return 
            for i in count:
                if count[i] > 0:
                    perm.append(i)
                    count[i] -= 1

                    backtracking(count,perm)

                    count[i]+=1
                    perm.pop()
        backtracking(count,[]) 
        return res
                
                
