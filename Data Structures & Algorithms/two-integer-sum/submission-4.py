class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indicies = {}

        for i, num in enumerate(nums):
            indicies[num] = i
        print(indicies)
        for i, num in enumerate(nums):
            remain = target - num
            print(remain)
            if remain in indicies and i != indicies[remain]:
                return [indicies[remain], i] if indicies[remain] < i else [i, indicies[remain]] 
            
        return []