class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,r = 0, len(s)-1        
        while l <= r:
            if s[l].isalnum():
                if s[r].isalnum():
                    if s[l].upper() != s[r].upper():
                        return False
                    r -= 1
                    l += 1
                    continue
                r -= 1 
                continue
            l += 1
            
        return True
