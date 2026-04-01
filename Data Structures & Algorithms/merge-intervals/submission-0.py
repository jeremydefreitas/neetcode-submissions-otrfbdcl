class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda pair: pair[0])
        res = [intervals[0]]

        for start, finish in intervals:
            if start <= res[-1][1]:
                res[-1][1] = max(res[-1][1], finish)
            else:
                res.append([start, finish])
        return res
        