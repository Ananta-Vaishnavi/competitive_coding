class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        keypad={"2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        ans=[]
        s=""
        if digits == "":
            return []
        def combinations(i,comb):
            if i == len(digits):
                ans.append(comb)
                return
            for x in keypad[digits[i]]:
                combinations(i+1,comb+x)
    
        combinations(0,"")
        return ans

        
