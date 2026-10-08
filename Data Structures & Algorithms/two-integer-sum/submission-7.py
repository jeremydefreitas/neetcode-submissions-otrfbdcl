class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}

        for i, num in enumerate(nums):
            need = target - num
            if need in indicies:
                return [indicies[need], i]
            else:
                indicies[num] = i

        return []