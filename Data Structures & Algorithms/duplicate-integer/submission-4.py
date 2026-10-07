class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()        #Originally had this outside the function, had memory of previous test cases so was not appropriate
        for i in nums:
            if i in seen:
                return True
            seen.add(i)
        return False
            



            
