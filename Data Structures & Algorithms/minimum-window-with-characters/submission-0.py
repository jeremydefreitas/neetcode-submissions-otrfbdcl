class Solution:
    def minWindow(self, s: str, t: str) -> str:
        tMap, sMap = {}, {}


        for i in range(len(t)):
            tMap[t[i]] = 1 + tMap.get(t[i], 0)
        
        l = 0
        have = 0
        need = len(tMap)
        length = float("infinity")
        res = [-1, -1]

        for r in range(len(s)):
            sMap[s[r]] = 1 + sMap.get(s[r], 0)
            if s[r] in tMap and sMap[s[r]] == tMap[s[r]]:
                have += 1
            while have == need:
                if (r - l + 1) < length:
                    length = r - l + 1
                    res = [l, r]

                sMap[s[l]] -= 1
                if s[l] in tMap and sMap[s[l]] < tMap[s[l]]:
                    have -= 1
                l += 1
        l, r = res
        return s[l : r + 1] if length != float("infinity") else ""


                


                    


        