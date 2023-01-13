class Solution:
    def partition(self, s: str) -> List[List[str]]:
        res = []
        def isPalindrome(s,l,r):
            while l <= r:
                if s[l] != s[r]:
                    return False
                l+=1
                r-=1
            return True
        
        def backtracking(start=0, pal=[]):
            if start == len(s):
                res.append(list(pal))
                return 
            for end in range(start,len(s)):
                if isPalindrome(s,start,end):
                    pal.append(s[start:end+1])
                    backtracking(end+1, pal)
                    pal.pop()
        backtracking()
        return res
