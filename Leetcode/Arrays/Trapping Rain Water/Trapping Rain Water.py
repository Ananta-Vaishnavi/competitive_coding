class Solution:
    def trap(self, height: List[int]) -> int:
        leftMax,rightMax=height[0],height[-1]
        left=0
        right=len(height)-1
        ans=0
        while left<right:
            if leftMax<rightMax:
                left+=1    
                leftMax=max(leftMax,height[left])
                ans+=leftMax-height[left]
                
            else:
                right-=1
                rightMax=max(rightMax,height[right])
                ans+=rightMax-height[right]
        return ans
                
