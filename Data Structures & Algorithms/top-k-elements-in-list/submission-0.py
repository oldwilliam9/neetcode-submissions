class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        d = {}
        for i in nums:
            if i not in d:
                d[i] = 0
            d[i]+=1
        ordered = sorted(d, key=d.get, reverse=True)
        return ordered[:k]