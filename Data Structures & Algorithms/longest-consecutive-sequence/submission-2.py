class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet = set(nums)
        res = 0
        for num in nums:
            if (num - 1) not in numSet:
                j = 1
                Longest = 1
                while (num + j) in numSet:
                    j += 1
                    Longest += 1
                res = max(res, Longest)
        return res


        

       

            
            