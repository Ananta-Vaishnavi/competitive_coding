class Solution:
	def NBitBinary(self, N):
	    ans=[] 
	    def helper(N,num,count_ones,count_zeroes):
	        if N==0:
	            ans.append(int(num))
	            return
	        helper(N-1,num+"1",count_ones+1,count_zeroes)
	        if count_ones > count_zeroes:
	            helper(N-1,num+"0",count_ones,count_zeroes+1)
	        
	    helper(N,"",0,0)
	    return ans


