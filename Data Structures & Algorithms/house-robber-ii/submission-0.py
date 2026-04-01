class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        


        def findMaxMoney(numsArr):
           
            n = len(numsArr)

            if n == 1:
                return numsArr[0]

            if n == 2:

                return max(numsArr[0], numsArr[1])
            cur = numsArr[0]
            prev = max(numsArr[0], numsArr[1])

            for i in range(2, n):
                cur, prev = prev, max(numsArr[i] + cur, prev)
            
            return prev

        
        return max(findMaxMoney(nums[1:]), findMaxMoney(nums[:-1]))

        
        