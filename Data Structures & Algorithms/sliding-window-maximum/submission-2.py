class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        l = 0
        if len(nums) == k and k == 1:
            return nums
        for r in range(len(nums)):
            if r - l + 1 == k:
                maximum = sorted(nums[l : r + 1])
                res.append(maximum[len(maximum) - 1])
                l += 1
        return res

        