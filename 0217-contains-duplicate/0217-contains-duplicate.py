class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        set1 = set(nums)

        return len(set1) < len(nums)