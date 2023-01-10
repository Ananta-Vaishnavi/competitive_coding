class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        
        
        def helper(ans, s, open, close):
            if open==0 and close==0:
                ans.append(s)
                
            if open>0:
                helper(ans, s+'(', open-1, close)
                
            if close>0 and open<close:
                helper(ans, s+')', open, close-1)
        
        ans = []
        helper(ans, '', n, n)
        
        return ans
