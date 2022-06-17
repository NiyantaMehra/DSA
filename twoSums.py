class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            ele = target - nums[i]
            if ele in d:
                key = d[ele]
                return [i,key]
            d[nums[i]] = i
        
        return []