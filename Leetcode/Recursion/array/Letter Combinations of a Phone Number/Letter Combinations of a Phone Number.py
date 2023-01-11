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
            combinations(i+1,comb+keypad[digits[i]][0])
            combinations(i+1,comb+keypad[digits[i]][1])
            combinations(i+1,comb+keypad[digits[i]][2])
            if digits[i] == "7" or digits[i] == "9":
                combinations(i+1,comb+keypad[digits[i]][3])
        combinations(0,"")
        return ans

        
