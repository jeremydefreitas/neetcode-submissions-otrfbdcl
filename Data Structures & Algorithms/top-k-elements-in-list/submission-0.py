class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        mapCount = {}
        for num in nums:
            mapCount[num] = mapCount.get(num, 0) + 1
        top_keys = sorted(mapCount, key=mapCount.get, reverse=True)[:k]
        return top_keys
        