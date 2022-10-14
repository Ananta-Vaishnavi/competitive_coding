class Solution:
    
    #Function to find minimum number of pages.
    def findPages(self,A, N, M):
        if M>N:
            return -1
        def isValid(mid,A,M):
            sum=0
            stu=1
            for i in range(len(A)):
                sum+=A[i]
                if sum>mid:
                    sum=A[i]
                    stu+=1
            if stu>M:
                return False
            else:
                return True

        start = max(A)
        end=sum(A)
        res=-1
        while(start<=end):
            mid=(start+end)//2
            if isValid(mid,A,M) !=0:
                res=mid
                end=mid-1
            else:
                start=mid+1
        return res
        
