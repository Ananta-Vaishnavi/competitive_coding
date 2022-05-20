Approach #1: Brute Force - Time Limit Exceeded

def containsDuplicate(self, nums: List[int]) -> bool:
    n = len(nums)
    for i in range(n - 1):
        for j in range(i + 1, n):
            if nums[i] == nums[j]: return True
    return False
Explanation: Use two for loops to compare pairs of integers in the array. Once we reach a comparison in which the numbers are the same, we return true. If we loop through all the integers of the array without reaching a similar pair of numbers, we return false.
Runtime: Time Limit Exceeded
Approach #2: Sorting

def containsDuplicate(self, nums: List[int]) -> bool:
    nums.sort()
    for i in range(len(nums)-1):
        if nums[i] == nums[i+1]: return True
    return False
Explanation: We start off by sorting the given array. Once we loop through the array from the beginning, if we see that the current number is the same as the next one in the array, there contains a duplicate in the array and therefore we return true. If we finish looping and there are no duplicates, we return false.
Runtime: Faster than 15% (715 ms)
Approach #3: Using Counter Function

def containsDuplicate(self, nums: List[int]) -> bool:
    freq = Counter(nums)
    for num, freq in freq.items():
        if freq > 1:
            return True
    return False
Explanation: Counter is a subclass of dict designed for counting hashable objects in Python. It’s a dictionary that stores the objects as keys and the frequencies of those objects as values. In this approach, we utilize Counter to count the frequencies of each integer for us. For example, if the input array is [1, 2, 3, 4, 4, 5], using Counter on that input array will give us the following dictionary: Counter({4: 2, 1: 1, 2: 1, 3: 1, 5: 1}). Utilizing this function, we will loop through the freq dictionary to see if any values (frequencies) are greater than 1, which means there exists an integer in the given array that is duplicated.
Runtime: Faster than 7% (797 ms)
Approach #4: Using Hashmap

def containsDuplicate(self, nums: List[int]) -> bool:
    counter = {}
    for num in nums:
        if num not in counter:
            counter[num] = 0
        counter[num] += 1
    for num, freq in counter.items():
        if freq > 1:
            return True
    return False
Explanation: In this approach, we essentially mimick what the Counter function does in the previous approach. We first initialize a hashmap, to which we loop through the given array and plot the frequencies of each integer by incrementing the values in the hashmap. Then, we try to look for a frequency that is greater than 1 and return the result accordingly.
Runtime: Faster than 7% (810 ms)
Approach #5: Using Set

def containsDuplicate(self, nums: List[int]) -> bool:
    return False if len(set(nums)) == len(nums) else True
def containsDuplicate(self, nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)
Explanation: This approach can be done a number of ways in just one line. Essentially we are using set() to convert the given array to a set. In a set, the values are unique and there exists no duplicates, therefore if the set version of the input array has a different length than the regular array itself, there exists a duplicate in the original input array.
Runtime: Faster than 5% (885 ms)
