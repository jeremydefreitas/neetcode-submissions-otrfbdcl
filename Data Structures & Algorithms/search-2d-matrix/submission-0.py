class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        def search(nums: List[int], t: int) -> int:
            l, r = 0, len(nums) - 1

            while l <= r:
                mid = (l + r) // 2
                if nums[mid] > t:
                    r = mid - 1
                elif nums[mid] < t:
                    l = mid + 1
                else: 
                    return mid
            return -1

        for i in matrix:
            if search(i, target) != -1:
                return True
        return False
        