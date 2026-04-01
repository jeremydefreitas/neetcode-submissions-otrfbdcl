class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        topRow, bottomRow = 0, ROWS - 1

        while topRow <= bottomRow:
            row = (topRow + bottomRow) // 2
            if matrix[row][-1] < target:
                topRow = row + 1
            elif matrix[row][0] > target:
                bottomRow = row - 1
            else:
                break

        if topRow > bottomRow:
            return False
        row = (topRow + bottomRow) // 2
        l, r = 0, COLS - 1

        while l <= r:
            mid = (l + r) // 2
            if matrix[row][mid] > target:
                r = mid - 1
            elif matrix[row][mid] < target:
                l = mid + 1
            else:
                return True
        return False


     
        