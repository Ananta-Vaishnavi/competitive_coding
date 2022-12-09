class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        mid=(2**(n-1))/2
        if n==1 or k==1:
            return 0
        elif k<=mid:
            return self.kthGrammar(n-1,k)
        else:
            return 1-(self.kthGrammar(n-1,k-mid))
