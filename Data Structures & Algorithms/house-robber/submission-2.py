class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        if n == 2:
            return max(nums[0], nums[1])
        

        cur = nums[0]
        prev = max(nums[0], nums[1])

        for i in range(2, n):
            cur, prev = prev, max(nums[i] + cur, prev)
            

        return prev
        

        