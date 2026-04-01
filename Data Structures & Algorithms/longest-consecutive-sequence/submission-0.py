class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        res = 0
        store = set(nums)
        for num in store:
            curr = 0 
            if (num - 1) not in store:
                while (num + curr) in store:
                    curr += 1
            res = max(res, curr)
        return res

            

        