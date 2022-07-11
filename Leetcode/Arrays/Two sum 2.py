#used two pointer method
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i=0
        j=len(numbers)-1
        while i<j:
            pointer1=numbers[i]
            pointer2=numbers[j]
            if pointer1+pointer2>target:
                j=j-1
            elif pointer1+pointer2<target:
                i=i+1
            else:
                return [i+1,j+1]
