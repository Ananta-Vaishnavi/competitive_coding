#step1:- We calculate the sum of the list
#step 2:- we calculate the sum of the numbers if all numbers we present if it were in a list
#step 3:- we return the difference
class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        return int((len(nums))*(len(nums)+1)/2-sum(nums))
