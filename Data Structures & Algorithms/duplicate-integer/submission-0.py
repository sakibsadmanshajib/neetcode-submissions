class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        dedup = list(set(nums))
        return len(dedup) != len(nums)