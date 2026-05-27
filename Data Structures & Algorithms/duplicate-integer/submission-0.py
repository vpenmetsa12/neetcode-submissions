class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nice = {}
        for x in nums:
            if x in nice:
                return True
            else:
                nice[x] = True
        return False
        