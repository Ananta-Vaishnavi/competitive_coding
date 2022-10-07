    def findFloor(self,A,N,X):
        if A[0]>X:
            return -1
        def modified_binary_search(l,target):
            res=0
            low=0
            high=len(l)-1
            while low<=high:
                mid=(low+high)//2
                if l[mid]>target:
                    high=mid-1
                else:
                    low=mid+1
                    res=mid
            return res
        return modified_binary_search(A,X)
