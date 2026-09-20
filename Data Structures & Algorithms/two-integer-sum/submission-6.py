class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}

        for i, num in enumerate(nums):
            indicies[num] = i

        for i, num in enumerate(nums):
            need = target - num
            if need in indicies and indicies[need] != i:
                return [i, indicies[need]]
        
        return []