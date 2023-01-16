class Solution:
    def minimumSum(self, num: int) -> int:
        res = [int(x) for x in str(num)]
        res.sort()
        tens = res[0] + res[1]
        ones = res[2] + res[3]
        return (tens*10+ones)
