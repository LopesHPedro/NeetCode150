class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        mapa = {}
        for i in range(len(nums)):
            palpite = target - nums[i]
            if palpite in mapa:
                return [i, mapa[palpite]] 
            mapa[nums[i]] = i
