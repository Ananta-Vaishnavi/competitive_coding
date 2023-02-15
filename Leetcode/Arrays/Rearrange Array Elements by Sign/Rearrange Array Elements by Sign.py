class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans = []
        pos, neg = 0,0

        while pos < n and neg < n:

            while nums[pos] < 0:
                pos += 1
            ans.append(nums[pos])

            while nums[neg] > 0:
                neg += 1
            ans.append(nums[neg])

            pos += 1
            neg += 1
        return ans
