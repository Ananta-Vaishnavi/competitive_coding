class Solution:
    def isValid(self, s: str) -> bool:
        # Assumptions
        # (){}[]
        # we only have brackets and nothing else
        # Invalid condition
        # ({})[]
        # stack = ( { 
        
        
        if len(s)%2!=0:
            return False
        
        dict={"(":")","{":"}","[":"]"}
        opn_bkts=["(","{","["]
        stack=[]
        op=0
        cp=0
        for i in s:
            if i in opn_bkts:
                stack.append(i)
                op+=1
            
            if i not in opn_bkts:
                cp+=1
                if stack:
                    if dict[stack[-1]] == i:
                        stack.pop()
                    else:
                        return False
        if cp>op:
            return False   
        elif len(stack)==0:
            return True
