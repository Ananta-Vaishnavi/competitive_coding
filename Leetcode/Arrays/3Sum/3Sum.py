class Solution(object):
    def threeSum(self, nums):
        nums.sort()
        answer=[]
        for i,a in enumerate(nums):
            if i>0 and a==nums[i-1]:
                continue
            left,right=i+1,len(nums)-1
            while left<right:
                if nums[left]+nums[right]+a>0:
                    right-=1
                elif  nums[left]+nums[right]+a<0:
                    left+=1
                else:
                    answer.append([a,nums[right],nums[left]])
                    left+=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1
        return answer
                    
