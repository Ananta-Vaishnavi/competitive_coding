class Solution:
    # Complete this function
    
    #Function to find equilibrium point in the array.
    def equilibriumPoint(self,A, N):
        if N == 1:
            return 1
        i = 0
        j = len(A)-1
        sum1 = A[i]
        sum2 = A[j]
        while i < j:
            if sum1 > sum2:
                j-=1
                sum2 += A[j]
                
            elif sum1 < sum2:
                i+=1
                sum1+= A[i]
                
            else:
                j-=1
                i+=1
                sum1+=A[i]
                sum2+=A[j]
                
        if A[i] == A[j] and i == j :
            return i+1
        return -1
