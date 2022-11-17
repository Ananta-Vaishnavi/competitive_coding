class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack=[]
        operators = ["+","-","/","*"]
        for i in tokens:
            if i in operators:
                a=stack.pop()
                b=stack.pop()
                ans=eval(str(b)+i+str(a))
                stack.append(int(ans))
            else:
                stack.append(i)
        return stack[0]
        
