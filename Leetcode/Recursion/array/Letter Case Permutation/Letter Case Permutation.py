class Solution:
    def letterCasePermutation(self, s: str) -> List[str]:
        def recursion (i,op):
            if i >= len(s):
                ans.append(op)
                return 
            if s[i].isdigit() == False:
                recursion(i+1, op+s[i])
                recursion(i+1, op+s[i].swapcase())
            else:
                recursion(i+1, op+s[i])
        ans = []
        recursion(0,"")
        return ans
