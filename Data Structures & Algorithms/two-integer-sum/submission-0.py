class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prevMap = {} #index is num and value position

        for index, val in enumerate(nums):
            remaining = (target - val)
            if remaining in prevMap: 
                return [prevMap[remaining], index]
            prevMap[val] = index

        