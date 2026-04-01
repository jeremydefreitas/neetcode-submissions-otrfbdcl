class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        test = set(nums)
        print(len(test))
        if len(nums) == len(test):
            return False
        return True
        