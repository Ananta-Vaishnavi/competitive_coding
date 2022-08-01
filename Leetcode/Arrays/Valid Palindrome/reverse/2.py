class Solution:
    def isPalindrome(self, s: str) -> bool:
        san = list(string.punctuation)
        san.append(' ')
        for i in san:
            s = s.replace(i,'')
        if s.lower() == s[::-1].lower():
            return True
        else:
            return False
