class Solution:
    def permutation (self, S):
        def sol(i,op):
            if i >= len(S):
                ans.append(op)
                return
            sol(i+1,op+" "+S[i])
            sol(i+1,op+S[i])
        ans=[]
        sol(1,S[0])
        return ans
   
