class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        string=""
        for i in s:
            if i.isalnum()==True:
                string+=i
        right,left=len(string)-1,0
        while left<right:
            if string[left]!=string[right]:
                return False
            right-=1
            left+=1
        return True
                
