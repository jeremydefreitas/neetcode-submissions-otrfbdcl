class Solution:
    def trap(self, height: List[int]) -> int:
        l, r = 0, len(height) - 1
        total = 0
        maxL = height[l]
        maxR = height[r]

        while l < r:
            if maxL < maxR:
                l += 1
                total += max(0, maxL - height[l])
            
            else: 
                
                r -= 1
                total += max(0, maxR - height[r])
            
            maxL = max(maxL, height[l])
            maxR = max(maxR, height[r])

        return total




        