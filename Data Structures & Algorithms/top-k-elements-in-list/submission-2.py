class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        for num in nums:
            freq[num] = 1 + freq.get(num, 0)

        sorted_dict = dict(sorted(freq.items(), key=lambda item: item[1],reverse=True))

        res = []
        for key in list(sorted_dict)[:k]:
            res.append(key)

        return res

     

        


        