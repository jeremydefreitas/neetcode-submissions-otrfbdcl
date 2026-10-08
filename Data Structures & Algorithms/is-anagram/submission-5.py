class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        sMap, tMap = {}, {}

        for i, c in enumerate(s):
            sMap[c] = 1 + sMap.get(c, 0)
            tMap[t[i]] = 1 + tMap.get(t[i], 0)

        return sMap == tMap



        
        


        

        