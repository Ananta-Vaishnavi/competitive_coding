class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_l=list(s)
        t_l=list(t)
        s_l.sort()
        t_l.sort()
        if s_l==t_l:
            return True
        else: 
            return False    
