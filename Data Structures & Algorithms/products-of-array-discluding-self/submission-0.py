class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        output = [0] * n
        for i in range(n):
            output[i] = 1
            for j in range (n):
                if i == j:
                    continue
                output[i] *= nums[j]
        return output

        

        