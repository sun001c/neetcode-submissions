class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remaining = {}
        for i in range(len(nums)):
            bal = target - nums[i]
            if bal in remaining:
                return [remaining[bal], i]
            else:
                remaining[nums[i]] = i