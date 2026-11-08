class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        count = {}
        for i in range(len(nums)):
            if nums[i] not in count:
                count[nums[i]] = 1
            else:
                count[nums[i]] += 1
        
        for k,v in count.items():
            if v > 1:
                return True
        return False