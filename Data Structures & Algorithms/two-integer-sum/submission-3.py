class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for n,i in enumerate(nums):
            rem = target - i
            if rem in d:
                return ([d[rem] , n])
            d[i]=n
        return False

        