class Solution:
    def romanToInt(self, s: str) -> int:
        symbols={"I":1,"V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}
        i=0
        sum=0
        while i<len(s):
            if i+1<len(s) and symbols[s[i]]<symbols[s[i+1]]:
                sum+=(symbols[s[i+1]]-symbols[s[i]])
                i+=2
            else:
                sum+=symbols[s[i]]
                i+=1
        return sum
