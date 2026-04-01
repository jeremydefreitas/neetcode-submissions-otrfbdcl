class MedianFinder:

    def __init__(self):
        self.arr = []
        

    def addNum(self, num: int) -> None:
        self.arr.append(num)
        

    def findMedian(self) -> float:
        self.arr.sort()
        print(self.arr)
        length = len(self.arr)

        if length == 1:
            return self.arr[0]
        isEven = False if length % 2 == 1 else True
        
        if not isEven and length > 1:
            mid = length // 2
            median = self.arr[mid]
            return float(median)
        elif isEven:
            mid = length // 2
            print(mid)
            median = (self.arr[mid - 1] + self.arr[mid]) / 2
            return median
        return 0.0

    [1, 3, 2]
        