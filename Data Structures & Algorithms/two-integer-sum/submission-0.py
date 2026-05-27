class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict = {}
        retVal = []
        for i in range(0,len(nums)):
            comp = target - nums[i]
            if comp in my_dict: 
                retVal.append(my_dict[comp])
                retVal.append(i)
                return retVal
            my_dict[nums[i]] = i
            
