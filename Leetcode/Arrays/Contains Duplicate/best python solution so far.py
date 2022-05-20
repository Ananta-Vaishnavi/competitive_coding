class Solution(object):
def containsDuplicate(self, nums):
    """
    :type nums: List[int]
    :rtype: bool
    """
    #this works on the fact that sets cannot contain duplicate values
    return len(nums) != len(set(nums))
